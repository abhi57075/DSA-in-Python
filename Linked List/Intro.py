class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode
    
    def listLength(self):
        length = 0
        currentNode = self.head
        while currentNode is not None:
            length+=1
            currentNode = currentNode.next
        return length

    def insertAt(self,newNode,position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
            
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode
    
    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print("Invalid position")
            return
        if self.isListEmpty() == True:
            print("Empty list")
            return
        if position is 0:
            self.deleteAt(0)
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            currentNode = currentNode.next
            currentPosition += 1


    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None
        del lastNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

firstNode = Node("John")
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode)
secondNode = Node("Albert")
linkedlist.insertEnd(secondNode)
thirdNode = Node("Ben")
linkedlist.insertEnd(thirdNode)
linkedlist.printList()
print("")
fourthNode = Node("Matthew")
linkedlist.insertHead(fourthNode)
linkedlist.printList()
print("")
fifthNode = Node("Denzel")
linkedlist.insertAt(fifthNode, 2)
linkedlist.printList()
print("")
linkedlist.deleteEnd()
print("")
linkedlist.deleteAt(2)
print("")


