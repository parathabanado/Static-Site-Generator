import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_tag_absent(self):
        node=HTMLNode()
        ans=node.props_to_html()
        self.assertEqual("",ans)  
    
    def test_props_present(self):
        props={"href":"https://www.google.com"}
        node=HTMLNode("<a>","Hello this is a link",None,props)
        ans=node.props_to_html()
        expected=""
        for key in props.keys():
            expected+=f' {key}="{props[key]}"'
        self.assertEqual(expected,ans)
    
    def test_props_present_multiple(self):
        props={
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node=HTMLNode("<a>","Hello this is a link",None,props)
        ans=node.props_to_html()
        expected=""
        for key in props.keys():
            expected+=f' {key}="{props[key]}"'
        self.assertEqual(expected,ans)
    
    def test_props_absent(self):
        node=HTMLNode("<p>","Hello this is a paragraph")
        ans=node.props_to_html()
        self.assertEqual("",ans)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node = LeafNode("a","This is a link",{"href":"https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">This is a link</a>')
    
    def test_leaf_no_tag(self):
        node=LeafNode("","Hello Duniya")
        self.assertEqual(node.to_html(),"Hello Duniya")
        node=LeafNode(None,"Hello World")
        self.assertEqual(node.to_html(),"Hello World")
    
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            node=LeafNode("p",None)
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_no_tag(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

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
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()