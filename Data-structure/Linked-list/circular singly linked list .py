class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class linkedlist:
  def __init__(self):
    self.head = None

  def length(self):
    currentNode = self.head
    length = 0
    while currentNode is not None and currentNode.next != self.head:
      length += 1
      currentNode = currentNode.next
    return length

  def insertAthead(self,data):
    newNode = Node(data)
    if not self.head:
      self.head = newNode
      self.head.next = self.head
    else:
      # the new node that we want to add before the head comes to play. from here we start traversing
      newNode.next = self.head
      currentNode = self.head
      while currentNode.next != self.head:
        currentNode = currentNode.next
      #we already knew that new node is already connected to its next(previous head) node
      #newNode.next = self.head
      currentNode.next = newNode
      self.head = newNode

  def insertAt(self,data,position):
    newNode = Node(data)
    if not self.head:
      print("the linked is empty.")
      return
    if position < 0 and position > self.length():
      print("invalid positon.")
      return
    if position == 0:
      self.insertAthead(newNode)
      return
    currentNode = self.head
    current_position = 0
    while currentNode is not None and current_position < position:
      previousNode = currentNode
      currentNode = currentNode.next
      current_position += 1
    if currentNode is None and current_position < position:
      print("out of bound")
    previousNode.next = newNode
    if currentNode is not None:
      newNode.next = currentNode

  def insertAtend(self,data):
    newNode = Node(data)
    if not self.head:
      self.head = newNode
      self.head.next = self.head
    currentNode = self.head
    while currentNode.next != self.head:
      currentNode = currentNode.next
    currentNode.next = newNode
    newNode.next = self.head

  def deleteAthead(self):
    if not self.head:
      print("the linked lists head is empty, nothing to delete.")
      return
    if self.head.next == self.head:
      self.head = None
      del self.head
      return
    currentNode = self.head
    while currentNode.next != self.head:
      currentNode = currentNode.next
    currentNode.next = self.head.next
    self.head = self.head.next
    #currentNode is the node that was previously the last node before the head. After adjusting pointers (currentNode.next = self.head.next and self.head = self.head.next), currentNode no longer serves any purpose in the list structure, so it is deleted.
    del currentNode

  def deleteAt(self,position):
    if not self.head:
      print("the link list is empty, nothing to delete.")
      return
    if position < 0 or position > self.length():
      print("invalid position.")
      return
    if position == 0:
      self.deleteAthead()
      return
    currentNode = self.head
    for i in range(position):
      previousNode = currentNode
      currentNode = currentNode.next
    previousNode.next = currentNode.next
    del currentNode
    if previousNode.next == self.head:
      self.head = previousNode.next

  def deleteAtend(self):
    if not self.head:
      print("the linked list is empty, no node to delete.")
      return
    if self.head.next == self.head:
      self.head = None
      return
    currentNode = self.head
    while currentNode.next != self.head:
      previousNode = currentNode
      currentNode = currentNode.next
    previousNode.next = self.head
    del currentNode

  #def print(self):
   # currentNode = self.head
    #if self.head:
     # while True:
      #  print(currentNode.data)
       # currentNode = currentNode.next
        #if currentNode == self.head:
         # break

  def print_ll(self):
    currentNode = self.head
    #self.head is just the starting point.we only increase and print the current node till currentNode == self.head to avoid the infinite loop
    while self.head is not None:
      print(currentNode.data)
      currentNode = currentNode.next
      if currentNode == self.head:
        break

cll = linkedlist()
cll.insertAtend(30)
cll.insertAtend(50)
cll.insertAtend(70)
cll.insertAtend(90)
cll.insertAthead(20)
cll.insertAt(100,0)
cll.deleteAtend()
cll.deleteAthead()
cll.deleteAt(3)
cll.print_ll()