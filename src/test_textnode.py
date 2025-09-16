import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a text node", TextType.BOLD, url="http://example.com")
        self.assertNotEqual(node, node4)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.BOLD)")

    def test_link_node(self):
        node = TextNode("This is a link", TextType.LINK, url="http://example.com")
        self.assertEqual(node.text, "This is a link")
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertEqual(node.url, "http://example.com")
        self.assertEqual(repr(node), "TextNode(This is a link, TextType.LINK, http://example.com)")
    
if __name__ == "__main__":
    unittest.main()