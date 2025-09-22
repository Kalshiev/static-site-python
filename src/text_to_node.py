from node_delimiter import split_nodes_link, split_nodes_delimiter, split_nodes_image
from textnode import TextType, TextNode

def text_to_textnodes(text):
    old_node = [TextNode(text, TextType.TEXT)]
    
    delimiter_types = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]

    for deli in delimiter_types:
        new_nodes = split_nodes_delimiter(old_node, deli[0], deli[1])
        old_node = new_nodes

    image_nodes = split_nodes_image(old_node)

    link_nodes = split_nodes_link(image_nodes)
    return link_nodes