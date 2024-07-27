class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxdepth(node):
    if node is None:
        return 0
    
    else:
        ldepth = maxdepth(node.left)
        rdepth = maxdepth(node.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1
        
root = Node(0)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(9)

print("Height of tree is", maxdepth(root))
