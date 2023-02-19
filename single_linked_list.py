class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linked:
    def __init__(self):
        self.head = None

    # function to show all nodes
    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    
    # function to display total number of nodes
    def length(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count+=1
        return count
    
    # function to add a node at the beginning of the list
    def addtop(self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    # function to add a node at the end of the list
    def addbottom(self,data):
        if self.head is None:
            self.addtop(data)
        else:
            newnode = node(data)
            newnode.next = None
            current = self.head
            for i in range(self.length()-1):
                current = current.next
            current.next = newnode
    
    # function to insert a node at particular index
    def insertatindex(self,data,index):
        if index < 0 or index > self.length():
            print("Invalid Index")
        elif index == 0:
            self.addtop(data)
        elif index == self.length():
            self.addbottom(data)
        else:
            newnode = node(data)
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            newnode.next = prev.next
            prev.next = newnode
    
    # function to delete a node at a particular index
    def deleteatindex(self,index):
        if index<0 or index>=self.length():
            print("Invalid index")
        elif index == 0:
            self.head = self.head.next
            print("Successfully deleted")
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            prev.next = prev.next.next
            print("Successfully deleted")

obj1 = linked()
obj1.addtop("Abhishek")
obj1.addtop("Atishay")
obj1.addtop("Aditya")
obj1.addtop("Aaagam")
obj1.addtop("Atharva")
obj1.addtop("Aahan")
obj1.addtop("Aarjav")
obj1.show()
print("\n")

obj1.addbottom('FAMILY')
obj1.show()
print("\n")

obj1.insertatindex('BROTHERS',4)
obj1.show()
print("\n")

print("Total no of elements in the linked list is: ", obj1.length())
print("\n")

obj1.deleteatindex(4)
obj1.show()
print("\n")


