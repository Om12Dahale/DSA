class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class createstack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
        
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
        
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode != None):
                print(iternode.data, end="")
                iternode = iternode.next
                if(iternode != None):
                    print(" -- ", end="")
            return

stack = createstack()
stack.push(10)
stack.push(12)
stack.push(17)

stack.display()

print("\nTop element:", stack.peek())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

stack.display()
