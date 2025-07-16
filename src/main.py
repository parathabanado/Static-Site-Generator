print("Hello World")
from textnode import *
from directory_copy import static_to_public
from page_generation import generate_page,generate_pages_recursive
import sys
def main():
    basepath="/"
    if len(sys.argv) > 1:
        basepath=sys.argv[1]
    print(basepath) #basepath="src/main.py"
    static_to_public()
    from_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/content"
    template_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/template.html"
    dest_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/docs"
    generate_pages_recursive(from_path,template_path,dest_path,basepath)
    
main()