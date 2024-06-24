class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return rest
    
    def __str__(self):
        linked_list_str = " "
        temp = self.head
        while temp:
            linked_list_str = (linked_list_str + str(temp.data) + " ")
            temp = temp.next
        return linked_list_str

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

linked_list = linked_list()
linked_list.push(5)
linked_list.push(8)
linked_list.push(20)
linked_list.push(16)

print("Given Linked List")
print(linked_list)

linked_list.head = linked_list.reverse(linked_list.head)

print("Reversed Linked List")
print(linked_list)