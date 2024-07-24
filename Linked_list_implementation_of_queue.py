class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return self.front == None
    
    def Enqueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def Dequeue(self):
        if self.isempty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

    def display(self):
        current = self.front
        if current is None:
            print("Queue is empty")
            return
        while current is not None:
            print(current.data, end="  < - ")
            current = current.next
        print("rear")

if __name__ == "__main__":
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(12)
    q.Dequeue
    q.Dequeue
    q.Enqueue(30)
    q.Enqueue(40)
    q.Enqueue(50)
    q.Dequeue()

    q.display()
    
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))

    