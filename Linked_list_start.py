class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_begining(self, data):
        node=Node(data, self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head 
        llstr=" "
        while itr:
            llstr=llstr + str(itr.data) + "--"
            itr=itr.next

        print(llstr)

if __name__ =="__main__":
    ll=linked_list()
    ll.insert_at_begining(5)
    ll.insert_at_begining(3)
    ll.insert_at_begining(7)
    ll.print()



        

    
