class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class stack:
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
  
  #function to push an element in the stack
  def push(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
  

  #function to pop an element from the stack
  def pop(self):
    if self.size() == 0:
      print('all elements are popped')
    else:
      self.head = self.head.next
      print('popped successfully')

obj1 = stack()
obj1.push("apple")
obj1.push('banana')
obj1.push("guava")
obj1.push("papaya")
obj1.push("mango")
obj1.show()
print("\n")

print("total elements : ",obj1.size())
print("\n")

obj1.pop()
obj1.show()
print("\n")