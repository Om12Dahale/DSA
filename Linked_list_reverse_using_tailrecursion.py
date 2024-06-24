class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def revserseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.revserseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return
        self.revserseUtil(self.head, None)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

llist = linked_list()
llist.push(5)
llist.push(7)
llist.push(79)
llist.push(64)

print("Given Linked List")
llist.printlist()

llist.reverse()

print("\nReversed Linked List")
llist.printlist()
