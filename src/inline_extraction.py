from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
        else:
            delim_count=node.text.count(delimiter)
            if delim_count%2!=0:
                raise Exception(f'Delimiter " {delimiter} " does not have a matching close')
            else:
                split_list=node.text.split(delimiter)
                if split_list[-1]=="":
                    split_list=split_list[:-1]
                if split_list[0]=="":
                    split_list=split_list[1:]
                    for i in range(len(split_list)):
                        if i%2==0:
                            new_nodes.append(TextNode(split_list[i],text_type))
                        else:
                            new_nodes.append(TextNode(split_list[i],TextType.TEXT))
                else:
                    for i in range(len(split_list)):
                        if i%2==0:
                            new_nodes.append(TextNode(split_list[i],TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(split_list[i],text_type))
    return new_nodes
                

def extract_markdown_images(text):
    matches=re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_markdown_links(text):
    matches=re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            matches=extract_markdown_images(node.text)
            match_set=set()
            for tup in matches:
                match_set.add(tup[0])
                match_set.add(tup[1])
            split_list=re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",node.text)
            split_set=set(split_list)
            text_set=split_set-match_set
            i=0
            while i < len(split_list):
                if split_list[i] in text_set:
                    if split_list[i]!="":
                        new_nodes.append(TextNode(split_list[i],TextType.TEXT))
                    i+=1
                else:
                    if i+1 < len(split_list):
                        new_nodes.append(TextNode(split_list[i],TextType.IMAGE,split_list[i+1]))
                        i+=2
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
        else:
            matches=extract_markdown_links(node.text)
            match_set=set()
            for tup in matches:
                match_set.add(tup[0])
                match_set.add(tup[1])
            split_list=re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",node.text)
            split_set=set(split_list)
            text_set=split_set-match_set
            i=0
            while i < len(split_list):
                if split_list[i] in text_set:
                    if split_list[i]!="":
                        new_nodes.append(TextNode(split_list[i],TextType.TEXT))
                    i+=1
                else:
                    if i+1 < len(split_list):
                        new_nodes.append(TextNode(split_list[i],TextType.LINK,split_list[i+1]))
                        i+=2
    return new_nodes
         

def text_to_textnode(text):
    node=TextNode(text,TextType.TEXT)
    delimiters=[["`",TextType.CODE],["_",TextType.ITALIC],["**",TextType.BOLD]]
    new_nodes=[node]
    code_split_nodes=split_nodes_delimiter(new_nodes,"`",TextType.CODE)
    italic_split_nodes=split_nodes_delimiter(code_split_nodes,"_",TextType.ITALIC)
    bold_split_nodes=split_nodes_delimiter(italic_split_nodes,"**",TextType.BOLD)
    image_split_nodes=split_nodes_image(bold_split_nodes)
    link_split_nodes=split_nodes_link(image_split_nodes)
    return link_split_nodes

