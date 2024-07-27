class newnode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def findmax(root):
    if root == None: 
        return float("-inf")
    
    res = root.data
    lres = findmax(root.left)
    rres = findmax(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res

def findmin(root):
    if root is None:
        return float("inf")
    
    res = root.data
    lres = findmin(root.left)
    rres = findmin(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res

if __name__ == "__main__":
    root = newnode(2)
    root.left = newnode(1)
    root.right = newnode(10)
    root.left.right = newnode(6)
    root.left.right.left = newnode(7)
    root.right.right = newnode(9)
    root.right.right.left = newnode(4)

    print("\nMaximum element is", findmax(root)) 
    print("Minimum element is", findmin(root))