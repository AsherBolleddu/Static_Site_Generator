from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal Text"
    BOLD_TEXT = "**Bold Text**"
    ITALIC_TEXT = "_Italic Text_"
    CODE_TEXT = "`Code Text`"
    LINK = "Link" # [anchor text](url)
    IMAGE = "Image" # ![alt text](url)

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"