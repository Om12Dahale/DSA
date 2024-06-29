class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        curr = Node()
        curr = self.head
        while(curr != None):
            print(curr.data, end=" ")
            curr = curr.next
        print()

head = Doublylinkedlist()
head.insert_at_begin(10)
head.insert_at_begin(12)
head.insert_at_begin(8)
head.insert_at_begin(19)    

print("List after inserting node at start")
head.printlist()
