import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "Hello", [], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    def test_props_to_html(self):
        node = HTMLNode("div", props={"class": "container", "id": "main"})
        self.assertEqual(
            node.props_to_html(), 
            ' class="container" id="main"'
            )

        node_no_props = HTMLNode("span")
        self.assertEqual(node_no_props.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Paragraph", None, {"style": "color:red"})
        self.assertEqual(
            repr(node), 
            "HTMLNode(tag=p, value=Paragraph, children=None, props={'style': 'color:red'})"
            )

class TestLeafNode(unittest.TestCase):
    def test_leafNode_to_html(self):
        leaf = LeafNode("span", "Text", props={"class": "highlight"})
        self.assertEqual(
            leaf.to_html(), 
            '<span class="highlight">Text</span>'
            )

    def test_leafNode_no_tag(self):
        leaf_no_tag = LeafNode(None, "Just text")
        self.assertEqual(
            leaf_no_tag.to_html(), 
            'Just text'
            )

    def test_leafNode_no_value(self):
        leaf_no_value = LeafNode("div", None)
        with self.assertRaises(ValueError):
            leaf_no_value.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span></div>"
            )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p", [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "italics"),
                LeafNode(None, "More Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(), 
            "<p><b>Bold Text</b>Normal Text<i>italics</i>More Normal Text</p>"
            )

    def test_parentNode_to_html(self):
        child1 = LeafNode("li", "Item 1")
        child2 = LeafNode("li", "Item 2")
        parent = ParentNode("ul", [child1, child2], props={"class": "list"})
        self.assertEqual(
            parent.to_html(), 
            '<ul class="list"><li>Item 1</li><li>Item 2</li></ul>'
            )

    def test_parentNode_no_tag(self):
        child = LeafNode("p", "Paragraph")
        parent_no_tag = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent_no_tag.to_html()

    def test_parentNode_no_children(self):
        parent_no_children = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_no_children.to_html()

if __name__ == "__main__":
    unittest.main()