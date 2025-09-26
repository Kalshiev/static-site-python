import os
from md_to_htmlNode import markdown_to_html_node
from markdown_regex import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    content_path = os.path.abspath(from_path)
    contents = os.listdir(content_path)
    for md_file in contents:
        file_check = os.path.join(content_path, md_file)
        if os.path.isfile(file_check) and md_file.endswith(".md"):
            with open(file_check) as md:
                markdown = md.read()
        else:
            return print(f"{md_file} not a markdown file")

    template = os.path.abspath(template_path)
    with open(template) as html:
        html_template = html.read()

    title = extract_title(markdown)
    body = markdown_to_html_node(markdown).to_html()

    final_html = html_template.replace("{{ Title }}", title).replace("{{ Content }}", body)
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    file = os.path.join(os.path.abspath(dest_path), "index.html")
    with open(file, "w") as out:
        out.write(final_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    source_dir = os.path.abspath(dir_path_content)
    destination = os.path.abspath(dest_dir_path)

    generate_page(source_dir, template_path, destination)

    dirs = os.listdir(source_dir)
    for dir in dirs:
        dir_path = os.path.join(source_dir, dir)
        if os.path.isdir(dir_path):
            new_destination = os.path.join(destination, dir)
            if not os.path.exists(new_destination):
                os.mkdir(new_destination)
            generate_page_recursive(dir_path, template_path, new_destination)
