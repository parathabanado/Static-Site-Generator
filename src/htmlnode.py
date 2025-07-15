class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props
    
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        str=""
        if self.props :
            for key in self.props.keys():
                str+=f' {key}="{self.props[key]}"'
        return str
    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag},\n Value: {self.value},\n Children: {self.children},\n Props: {self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag,value,None,props)
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or self.tag=="":
            return self.value
        ans=f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return ans    
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    
    def __repr__(self):
        return f"PaNode(Tag: {self.tag},\n Children: {self.children},\n Props: {self.props})"

    def to_html(self):
        if self.tag is None or self.tag=="":
            raise ValueError("invalid html: No html tag")
        if self.children is None or len(self.children)==0:
            raise ValueError("invalid html: No children")
        else:
            ans=f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                ans+=child.to_html()
            ans+=f'</{self.tag}>'
            return ans
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

# node =ParentNode("h1", [LeafNode(None, "Tolkien Fan Club", None)], None)
# html=node.to_html()
# print(html)



        
    