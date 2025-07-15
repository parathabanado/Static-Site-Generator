print("Hello World")
from textnode import *
from directory_copy import static_to_public
from page_generation import generate_page,generate_pages_recursive
def main():
    static_to_public()
    from_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/content"
    template_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/template.html"
    dest_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/public"
    generate_pages_recursive(from_path,template_path,dest_path)
    # from_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/content/index.md"
    # template_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/template.html"
    # dest_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/public/index.html"
    # generate_page(from_path,template_path,dest_path)
    
    # from_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/content/contact/index.md"
    # dest_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/public/contact/index.html"
    # generate_page(from_path,template_path,dest_path)
    
    # from_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/content/blog/glorfindel/index.md"
    # dest_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/public/blog/glorfindel/index.html"
    # generate_page(from_path,template_path,dest_path)
    
    # from_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/content/blog/majesty/index.md"
    # dest_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/public/blog/majesty/index.html"
    # generate_page(from_path,template_path,dest_path)
    
    # from_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/content/blog/tom/index.md"
    # dest_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/public/blog/tom/index.html"
    # generate_page(from_path,template_path,dest_path)

main()