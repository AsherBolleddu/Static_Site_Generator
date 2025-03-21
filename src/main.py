from textnode import TextNode, TextType

def main():
    temp = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(temp)

if __name__ == "__main__":
    main()