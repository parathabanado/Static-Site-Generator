from textnode import *
from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_extraction import *
import re
class BlockType(Enum):
    PARA="paragrapgh"
    HEAD="heading"
    CODE="code"
    QUOTE="quote"
    ULIST="unordered_list"
    OLIST="ordered_list"

def markdown_to_blocks(markdown):
    split_list=markdown.split("\n\n")
    ans=[]
    for i in range(len(split_list)):
        split_list[i]=split_list[i].strip()
        if split_list[i]!='':
            ans.append(split_list[i])
    return ans


def block_to_block_type(block):
    lines = block.split("\n")
    tag=None
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        count=0
        for ch in block:
            if ch!="#":
                break
            count+=1
            if count>=6:
                break
        if count!=0:
            tag=f"h{count}"
        return BlockType.HEAD,tag
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE,"code"
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARA,"p"
        return BlockType.QUOTE,"blockquote"
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARA,"p"
        return BlockType.ULIST,"ul"
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARA,"p"
            i += 1
        return BlockType.OLIST,"ol"
    return BlockType.PARA,"p"

def text_to_children(text):
    children_text_nodes=[]
    lines=text.split("\n")
    for i in range(len(lines)):
        if i==len(lines)-1:
            line = lines[i]
            if line.startswith("- "):
                li_children=text_to_children(line[2:])
                li_node=ParentNode("li",li_children,None)
                children_text_nodes.append(li_node)
            elif re.match(r"^\d+\.\s", line):
                li_children=text_to_children(line[3:])
                li_node=ParentNode("li",li_children,None)
                children_text_nodes.append(li_node)
            else:
                children_text_nodes.extend(text_to_textnode(f"{lines[i]}"))
        else:
            line = lines[i]
            if line.startswith("- "):
                li_children=text_to_children(line[2:])
                li_node=ParentNode("li",li_children,None)
                children_text_nodes.append(li_node)
            elif re.match(r"^\d+\.\s", line):
                li_children=text_to_children(line[3:])
                li_node=ParentNode("li",li_children,None)
                children_text_nodes.append(li_node)
            else:
                children_text_nodes.extend(text_to_textnode(f"{lines[i]} "))
    children_html_nodes=[]
    for child in children_text_nodes:
        try:
            if child.text and child.text_type:
                children_html_nodes.append(text_node_to_html_node(child))
        except Exception:
            children_html_nodes.append(child)
    return children_html_nodes

def markdown_to_html_node(markdown):
    blocks=markdown_to_blocks(markdown)
    div_node=ParentNode("div",[],None)
    for block in blocks:
        block_type,tag=block_to_block_type(block)
        if block_type==BlockType.CODE:
            lines=block.split("\n")
            code_text=""
            for line in lines:
                if line!="```":
                    code_text+=line+"\n"
            text_node=TextNode(code_text,TextType.CODE,None)
            code_node=text_node_to_html_node(text_node)
            pre_node=ParentNode("pre",[code_node],None)
            div_node.children.append(pre_node)
        elif block_type==BlockType.QUOTE:
            quote_text=""
            lines=block.split("\n")
            for line in lines:
                quote_text+=line[2:]+" " 
            children=text_to_children(quote_text[:-1])
            block_node=ParentNode(tag,children,None)
            div_node.children.append(block_node)
        elif block_type==BlockType.HEAD:
            children=text_to_children(block[int(tag[-1])+1:])
            block_node=ParentNode(tag,children,None)
            div_node.children.append(block_node)
        else:
            children=text_to_children(block)
            block_node=ParentNode(tag,children,None)
            div_node.children.append(block_node)
    return div_node


def extract_title(markdown):
    blocks=markdown_to_blocks(markdown)
    ans=""
    for block in blocks:
        block_type,tag=block_to_block_type(block)
        if tag=="h1":
            return block.split("\n")[0][2:].strip()
    raise Exception("h1 Header not found")

md='''
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

## Reasons I like Tolkien

- You can spend years studying the legendarium and still not understand its depths
- It can be enjoyed by children and adults alike
- Disney _didn't ruin it_ (okay, but Amazon might have)
- It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Aiya, Ambar!")
}
```

Want to get in touch? [Contact me here](/contact).

This site was generated with a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev).
'''

# node=markdown_to_html_node(md)
# print(node)
