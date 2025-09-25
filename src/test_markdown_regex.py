import unittest

from markdown_regex import extract_markdown_links, extract_markdown_images, extract_title

class TestMarkdownRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is a link [link](http://biblioteca.uci.edu.mx)"
        )
        self.assertListEqual([("link","http://biblioteca.uci.edu.mx")], matches)

    def test_extract_title(self):
        matches = extract_title(
            """
        # Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.
        """
        )
        self.assertEqual("Tolkien Fan Club", matches)