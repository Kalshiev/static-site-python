import os
from md_to_htmlNode import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    content_path = os.path.abspath(from_path)
    contents = os.listdir(content_path)
    for md_file in contents:
        if md_file.endswith(".md"):
            with open(os.path.join(content_path, md_file)) as md:
                markdown = md.read()

    template = os.path.abspath(template_path)
    with open(template) as html:
        html_template = html.read()

    


generate_page("./content", "template.html", "")