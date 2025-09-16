import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_html import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
    def test_text_to_html(self):
        node = TextNode("This is a text node.", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node.")

    def test_text_to_html_with_formatting(self):
        node = TextNode("This is bold text.", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text.")

    def test_text_to_html_with_italic(self):
        node = TextNode("This is italic text.", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text.")

    def test_text_to_html_code(self):
        node = TextNode("This is code text.", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text.")

    def test_text_to_html_link(self):
        node = TextNode("Click here", TextType.LINK, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "http://example.com"})

    def test_text_to_html_image(self):
        node = TextNode("Image description", TextType.IMAGE, url="http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, HTMLNode)
        self.assertEqual(html_node.tag, "img")
        self.assertIsNone(html_node.value)
        self.assertEqual(html_node.props, {"src": "http://example.com/image.png", "alt": "Image description"})