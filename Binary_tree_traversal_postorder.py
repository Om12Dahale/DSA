class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postordertraversal(node):
    if node is None:
        return
    postordertraversal(node.left)
    postordertraversal(node.right)
    print(node.data, end = " ")

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("postorder Traversal :", end = " ")
    postordertraversal(root)
    print()

if __name__ == "__main__":
    main()