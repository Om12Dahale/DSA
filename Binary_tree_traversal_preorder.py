class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preordertraversal(root):
    if root is None:
        return
    print(root.data, end = " ")
    preordertraversal(root.left)
    preordertraversal(root.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder Traversal:", end = " ")
    preordertraversal(root)
    print()

if __name__ == "__main__":
    main()