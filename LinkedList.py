'''|20|-|--->| 45|-|--->|10|-|--->|0| |'''

class Node:
    def __init__(self,value):
        self.value=value
       # self.front=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def addelement(self,value):
        t=Node(value)
        tail=self.head
        if self.head is None:
            self.head=t
        else:
            while tail.next is not None:
                tail=tail.next

            tail.next=t
    #Inserting elements in front of the list
      #  else:
      #      t.next=self.head
      #      self.head=t

    def delelement(self):
        pass

    def viewelements(self):
        while self.head != None:
            print(self.head.value)
            print(id(self.head))
            self.head = self.head.next


n=int(input("Enter the number of elements:"))
inpli=[]
print("Enter the elements:")
for _  in range(n):
    inpli.append(input())

print("Creating Doubly Linked List...")

dll=LinkedList()
for i in inpli:
    dll.addelement(i)

dll.viewelements()




