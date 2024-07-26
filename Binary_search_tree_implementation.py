class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node

def search(root, key):
    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)

    return search(root.left, key)

if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 10)
    insert(root, 11)
    insert(root, 13)
    insert(root, 17)
    insert(root, 19)
    insert(root, 21)

    key = 12
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")

    key = 13
    if search(root, key) is None:
        print(key, "Not found")
    else:
        print(key, "found")


    
