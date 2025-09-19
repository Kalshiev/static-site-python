import unittest

from textnode import TextNode, TextType
from node_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode(
            "This text has no images", TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This text has no images", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_image_before_text(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) This is an image", TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is an image", TextType.TEXT)
            ],
            new_nodes
        )
