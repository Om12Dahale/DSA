class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxValue(root):
    if root == None: 
        return float("-inf")
    
    res = root.data
    lres = maxValue(root.left)
    rres = maxValue(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res

def minValue(root):
    if root is None:
        return float("inf")
    
    res = root.data
    lres = minValue(root.left)
    rres = minValue(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res
     
def isBST(node):
    if node is None:
        return True
    
    if(node.left is not None and maxValue(node.left) > node.data):
        return False
    
    if(node.right is not None and minValue(node.right) < node.data):
        return False
    
    if(isBST(node.left) is False or isBST(node.right) is False):
        return False
    
    return True

if __name__ == "__main__":
  root = Node(4)
  root.left = Node(2)
  root.right = Node(5)
  #root.right.left = Node(7)
  root.left.left = Node(1)
  root.left.right = Node(3)

  if isBST(root) is True:
      print("Is BST")
  else:
      print("Not a BST")
