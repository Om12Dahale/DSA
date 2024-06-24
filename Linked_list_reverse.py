class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

llist = Linkedlist()
llist.push(6)
llist.push(18)
llist.push(20)
llist.push(30)

print("Given Linked List")
llist.printlist()
llist.reverse()
print("\nReversed Linked List")
llist.printlist()

