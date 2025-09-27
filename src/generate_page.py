import os
from md_to_htmlNode import markdown_to_html_node
from markdown_regex import extract_title

def generate_page_markdown(md_path, template_path, dest_path, basepath):
    print(f"Generating page from {md_path} to {dest_path}")
    if not md_path.endswith(".md"):
        return print(f"{md_path} not a markdown file")
    else:
        md = open(md_path)
        markdown = md.read()
    template = os.path.abspath(template_path)
    with open(template) as html:
        html_template = html.read()
    title = extract_title(markdown)
    body = markdown_to_html_node(markdown).to_html()
    final_html = html_template.replace("{{ Title }}", title).replace("{{ Content }}", body)
    final_html = final_html.replace('href="/', f'href={basepath}').replace('src="/', f'src={basepath}')
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    file = os.path.join(os.path.abspath(dest_path), "index.html")
    with open(file, "w") as out:
        out.write(final_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)
    for file in files:
        if file == "index.md":
            md_path = os.path.join(dir_path_content, file)
            dest_path = os.path.join(dest_dir_path, os.path.relpath(dir_path_content, dir_path_content))
            generate_page_markdown(md_path, template_path, dest_path, basepath)
        else:
            generate_page_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file), basepath)
