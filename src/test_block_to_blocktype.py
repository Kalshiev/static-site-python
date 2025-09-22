import unittest

from block_to_blocktype import block_to_blocktype, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_blocktype(self):
        heading = "# A sample heading"
        case = block_to_blocktype(heading)
        self.assertEqual(BlockType.HEADING, case)