class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class queue:
  def __init__(self):
    self.head = None
  
  #function to show all the elements
  def show(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

  #function to display total no. of elements
  def size(self):
    current = self.head
    count = 0
    while current is not None:
      current = current.next
      count = count + 1
    
    return count
  
  #function to insert an element in the queue
  def insert(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
  

  #function to delete an element from the queue
  def delete(self):
      if self.head is None:
        print('empty queue')
      elif self.head.next is None:
        self.head = None
      elif self.size() == 2:
        self.head.next = None
      else:
        current = self.head
        for i in range(self.size()-2):
          current = current.next
        current.next = None

obj1 = queue()
obj1.insert("apple")
obj1.insert('banana')
obj1.insert("guava")
obj1.insert("papaya")
obj1.insert("mango")
obj1.show()
print("\n")

print("total elements : ",obj1.size())
print("\n")

obj1.delete()
obj1.show()
print("\n")