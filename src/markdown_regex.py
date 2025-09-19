import re

def extract_markdown_images(text):
    links = []
    alt_text = re.findall(r"!\[([^\[\]]*)\]\([^\(\)]*\)", text)
    link = re.findall(r"!\[[^\[\]]*\]\(([^\(\)]*)\)", text)

    for i in range(len(link)):
        links.append((alt_text[i], link[i]))
    
    return links

def extract_markdown_links(text):
    links = []
    alt_text = re.findall(r"\[([^\[\]]*)\]\([^\(\)]*\)", text)
    link = re.findall(r"\[[^\[\]]*\]\(([^\(\)]*)\)", text)

    for i in range(len(link)):
        links.append((alt_text[i], link[i]))

    return links
