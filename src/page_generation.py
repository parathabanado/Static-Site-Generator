from markdown_blocks import markdown_to_html_node,extract_title
from htmlnode import HTMLNode, LeafNode, ParentNode
from directory_copy import static_to_public
import os
import shutil
def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_contents=""
    with open(from_path, 'r') as from_object:
        from_contents = from_object.read()
    template_contents=""
    with open(template_path, 'r') as template_object:
        template_contents = template_object.read()
    title=extract_title(from_contents)
    node=markdown_to_html_node(from_contents)
    html=node.to_html()
    print(html)
    template_contents=template_contents.replace("{{ Title }}",title)
    template_contents=template_contents.replace("{{ Content }}",html)
    try:
        dest_dir_path = os.path.dirname(dest_path)
        if dest_dir_path != "":
            os.makedirs(dest_dir_path, exist_ok=True)
        with open(dest_path, 'w') as dest_object:
            dest_object.write(template_contents)
        print("Successfully written")
    except Exception as e:
        print("Error writing :",e)


def recur_generate(source,template,dest):
    if not os.path.exists(dest):
        print("Hi")
        os.mkdir(dest)
    if os.path.exists(source):
        list_dir=os.listdir(source)
        for item in list_dir:
            if os.path.isfile(os.path.join(source,item)):
                root, ext = os.path.splitext(os.path.join(source,item))
                if ext==".md":
                    dest_file=item.replace(".md",".html")
                    generate_page(os.path.join(source,item),template,os.path.join(dest,dest_file))
            else:
                recur_generate(os.path.join(source,item),template,os.path.join(dest,item))
        return
    else:
        raise Exception("Source Destination invalid")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dest_dir_path):
        try:
            shutil.rmtree(dest_dir_path)
        except OSError as e:
            print(f"Error: could not delete {dest_dir_path} : {e}") 
    static_to_public()
    recur_generate(dir_path_content,template_path,dest_dir_path)