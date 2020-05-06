'''|20|-|--->| 45|-|--->|10|-|--->|0| |'''

class Node:
    def __init__(self,value):
        self.value=value
        self.front=None
        self.next=None

class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addelement(self,value):
        t=Node(value)

        if self.head is None:
            self.head=t
            self.tail=t
        elif self.head is self.tail:
            self.tail=t
            self.tail.front=self.head
            self.head.next=self.tail
        else:
            self.tail.next=t
            t.front=self.tail
            self.tail=t


    def delelement(self):
        pass

    def viewelements(self):
        print("Printing from head ...")
        while self.head != None:
            print(self.head.value)
            self.head = self.head.next
        print("Printing from tail ...")
        while self.tail != self.head:
            print(self.tail.value)
            self.tail=self.tail.front



n=int(input("Enter the number of elements:"))
inpli=[]
print("Enter the elements:")
for _  in range(n):
    inpli.append(input())

print("Creating Doubly Linked List...")

dll=DLinkedList()
for i in inpli:
    dll.addelement(i)

dll.viewelements()




