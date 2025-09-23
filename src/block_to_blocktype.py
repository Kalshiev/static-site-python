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
    s = md_block.lstrip()
    
    if re.match(r'^#{1,6}\s', s):
        return BlockType.HEADING
    
    if md_block.startswith("```") and md_block.rstrip().endswith("```"):
        return BlockType.CODE
    
    if re.match(r"^>\s", s):
        return BlockType.QUOTE
    
    if re.match(r"^-\s", s):
        return BlockType.UNORDERED
    
    if re.match(r"^\d+\.\s", s):
        return BlockType.ORDERED
    
    return BlockType.PARAGRAPH