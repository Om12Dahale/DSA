class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def printlist(self, node):
        while node is not None:
            print(node.data, end = " ")
            node = node.next

if __name__ == "__main__":
    dll = Doublylinkedlist()
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)
 
    print("Original Linked List")
    dll.printlist(dll.head)
    dll.reverse()
    print("\nReversed Linked List")
    dll.printlist(dll.head)