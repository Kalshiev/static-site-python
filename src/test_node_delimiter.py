import unittest

from textnode import TextNode, TextType
from node_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_texts = [
            "This is text with a ",
            "code block",
            " word"
        ]
        expected_types = [
            TextType.TEXT,
            TextType.CODE,
            TextType.TEXT
        ]

        self.assertEqual(len(new_nodes), 3)
        for new_node, expected_text, expected_type in zip(new_nodes, expected_texts, expected_types):
            self.assertEqual(new_node.text, expected_text)
            self.assertEqual(new_node.text_type, expected_type)