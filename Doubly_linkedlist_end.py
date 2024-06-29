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
    
    def insert_at_end(self, new_data):
        new_node = Node(data = new_data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_data
            return

        while(last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last


    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        curr = Node()
        curr = self.head
        while(curr != None):
            print(curr.data, end = " ")
            curr = curr.next
        print()

head = Doublylinkedlist()
head.insert_at_begin(10)
head.insert_at_begin(12)
head.insert_at_begin(8)
head.insert_at_begin(19) 

head.insert_at_end(48)
head.insert_at_end(58)
head.insert_at_end(68)
head.insert_at_end(78)    

print("List after inserting node at end")
head.printlist()