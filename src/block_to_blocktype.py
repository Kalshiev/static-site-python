import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def block_to_blocktype(md_block):
    if re.search(r'#{1,6}\s', md_block):
        return BlockType.HEADING
    if md_block.startswith("```") and md_block.endswith("```"):
        return BlockType.CODE
    if md_block.startswith(">"):
        return BlockType.QUOTE
    if md_block.startswith("-"):
        return BlockType.UNORDERED
    if re.search(r'[0-9].\s', md_block):
        return BlockType.ORDERED
    return BlockType.PARAGRAPH