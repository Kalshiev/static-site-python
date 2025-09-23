import unittest

from block_to_blocktype import block_to_blocktype, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_blocktype_heading(self):
        heading = "# A sample heading"
        case = block_to_blocktype(heading)
        self.assertEqual(BlockType.HEADING, case)

    def test_block_to_blocktype_code(self):
        code = "```A code block```"
        case = block_to_blocktype(code)
        self.assertEqual(BlockType.CODE, case)

    def test_block_to_blocktype_quote(self):
        quote = "> A sample quote"
        case = block_to_blocktype(quote)
        self.assertEqual(BlockType.QUOTE, case)

    def test_block_to_blocktype_unordered(self):
        unordered = "- A sample unordered list"
        case = block_to_blocktype(unordered)
        self.assertEqual(BlockType.UNORDERED, case)

    def test_block_to_blocktype_ordered(self):
        ordered = "1. A sample ordered list"
        case = block_to_blocktype(ordered)
        self.assertEqual(BlockType.ORDERED, case)