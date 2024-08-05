class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inordersuccessor(n):
    if n.right is not None:
        return minvalue(n.right)
    
    p = n.parent
    while p is not None:
        if n!= p.right:
            break
        n = p
        p = p.parent
    return p

def minvalue(node):
    current = node
    while current is not None:
        if current.left is None:
            break
        current = current.left

    return current

def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node

        return node
    
if __name__ == "__main__":

    root = None
    root = insert(root, 20)
    root = insert(root, 8)  
    root = insert(root, 22)  
    root = insert(root, 4)
    root = insert(root, 12)
    root = insert(root, 10)          
    root = insert(root, 14)  
    temp = root.left.right.right

    succ = inordersuccessor(temp)
    if succ is not None:
        print("Inorder Successor of", temp.data, "is", succ.data)
    else:
        print("Inorder Successor doesn't exist")