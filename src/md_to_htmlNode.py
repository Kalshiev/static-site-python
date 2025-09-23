from md_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_blocktype, BlockType
from text_to_html import text_node_to_html_node
from text_to_node import text_to_textnodes
from htmlnode import LeafNode, ParentNode
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlnodes = []
    for block in blocks:
        blocktype = block_to_blocktype(block)
        if blocktype is BlockType.PARAGRAPH:
            lines = [ln.strip() for ln in block.splitlines()]
            text = " ".join([ln for ln in lines if ln])
            if text:
                htmlnodes.append(text_to_children(text, "paragraph"))
        elif blocktype is BlockType.HEADING:
            count = 0
            for b in block:
                if b != "#":
                    break
                count += 1
            block = block[count:].lstrip()
            htmlnodes.append(text_to_children(block, "heading", count))
        elif blocktype is BlockType.UNORDERED:
            li_nodes = []
            for line in block.splitlines():
                if line.lstrip().startswith("- "):
                    s = line.lstrip()
                    li_nodes.append(text_to_children(s[2:], "list"))
            htmlnodes.append(
                ParentNode("ul", li_nodes)
            )
        elif blocktype is BlockType.QUOTE:
            quote_nodes = []
            fullquote = ""
            for line in block.splitlines():
                if line.strip().startswith("> "):
                    s = line.lstrip()
                    fullquote += f"\n{s[2:]}"
            quote_nodes.append(text_to_children(fullquote, "quote"))
            htmlnodes.append(
                ParentNode("blockquote", quote_nodes)
            )
        elif blocktype is BlockType.ORDERED:
            li_nodes = []
            for line in block.splitlines():
                s = line.lstrip()
                m = re.match(r"^(\d+)\.\s", s)
                if m:
                    li_nodes.append(text_to_children(s[m.end():], "list"))
            htmlnodes.append(
                ParentNode("ol", li_nodes)
            )
        elif blocktype is BlockType.CODE:
            lines = block.splitlines()
            inner_lines = lines[1:-1]
            import textwrap
            inner = textwrap.dedent("\n".join(inner_lines)).lstrip("\n").rstrip() + "\n"
            code_leaf = LeafNode(None, inner)
            code_node = ParentNode("code", [code_leaf])
            htmlnodes.append(ParentNode("pre", [code_node]))

    parent = ParentNode("div", htmlnodes)
    
    return parent

def text_to_children(block, blocktype, hcount=0):
    text_nodes = text_to_textnodes(block)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    if blocktype == "paragraph":
        children_nodes = ParentNode("p", children)
    elif blocktype == "heading":
        children_nodes = ParentNode(f"h{hcount}", children)
    elif blocktype == "list":
        children_nodes = ParentNode("li", children)
    elif blocktype == "quote":
        children_nodes = ParentNode("p", children)
    return children_nodes