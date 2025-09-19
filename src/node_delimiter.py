from textnode import TextNode, TextType
from markdown_regex import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            for part in parts:
                if part == delimiter:
                    continue
                if part == parts[0] or part == parts[-1]:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        text = node.text
        for image in images:
            parts = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(parts[0]) != 0:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = parts[1]
        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        text = node.text
        for link in links:
            parts = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(parts[0]) != 0:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = parts[1]
        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes