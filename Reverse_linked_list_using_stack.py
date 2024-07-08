class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data, self.head)
        self.head = new_node

    def reverselist(self):
        stack = []

        ptr = self.head
        while ptr.next != None:
            stack.append(ptr)
            ptr = ptr.next

        self.head = ptr
        while len(stack) != 0:
            ptr.next = stack.pop()
            ptr = ptr.next

        ptr.next = None

    def printlist(self):
        curr = self.head
        while curr:
            print(curr.data, end = " ")
            curr = curr.next

if __name__ == "__main__":

    linkedlist = Linkedlist()
    linkedlist.push(1)
    linkedlist.push(8)
    linkedlist.push(5)
    linkedlist.push(9)
    linkedlist.push(3)
    
    
    print("Given linked list")
    linkedlist.printlist()

    linkedlist.reverselist()
    print("\nReversed linked list")  
    linkedlist.printlist()

