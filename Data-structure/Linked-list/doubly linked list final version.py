class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None

class linkedlist:
  def __init__(self):
    self.head = None

  def length(self):
    currentNode = self.head
    length = 0
    while currentNode is not None:
      length += 1
      currentNode = currentNode.next
    return length

  def insertAthead(self,data):
    newNode = Node(data)
    if self.head is not None:
      self.head.prev = newNode
      newNode.next = self.head
    self.head = newNode

  def insertAt(self,data,position):
    newNode = Node(data)
    if self.head is None:
      print("the list is empty.")
      return
    if position < 0 or position > self.length():
      print("invalid position")
      return
    if position == 0:
      self.insertAthead(data)
      return
    currentNode = self.head
    current_position = 0
    while currentNode is not None and current_position < position:
      previousNode = currentNode
      currentNode = currentNode.next
      current_position += 1
    if currentNode is None and current_position < position:
      print("out of bound.")
      return
    previousNode.next = newNode
    newNode.prev = previousNode
    if currentNode is not None:
      newNode.next = currentNode
      currentNode.prev = newNode

  def insertAtend(self,data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      return
    currentNode = self.head
    while True:
      if currentNode.next is None:
        break
      currentNode = currentNode.next
    currentNode.next = newNode
    newNode.prev = currentNode

  def deleteAthead(self):
    if self.head is None:
      print("the linked lists head is empty.")
      return
    if self.head.next is None:
      self.head = None
      del self.head
      return
    self.head = self.head.next
    self.head.prev = None

  def deleteAt(self,position):
    if self.head is None:
      print("the linked list is empty.")
      return
    if position < 0 or position >= self.length():
      print("invalid positon.")
      return
    if position == 0:
      self.deleteAthead()
      return
    currentNode = self.head
    current_position = 0
    while currentNode is not None and current_position < position:
      currentNode = currentNode.next
      current_position += 1
    if currentNode is None:
      print("out of bound")
    currentNode.prev.next = currentNode.next
    if currentNode.next is not None:
      currentNode.next.prev = currentNode.prev
    del currentNode

  def deleteAtend(self):
    if self.head is None:
      print("the linked list is empty. no element to delete.")
      return
    currentNode = self.head
    if currentNode.next is None:
      currentNode = None
      del currentNode
    else:
      while currentNode.next is not None:
        currentNode = currentNode.next
      currentNode.prev.next = None
      del currentNode

  def print_ll(self):
    currentNode = self.head
    while True:
      if currentNode is None:
        break
      print(currentNode.data)
      currentNode = currentNode.next

dll = linkedlist()
dll.insertAtend(100)
dll.insertAtend(120)
dll.insertAtend(140)
dll.insertAtend(160)
dll.insertAthead(90)
dll.insertAt(130,3)
dll.deleteAtend()
dll.deleteAthead()
dll.deleteAt(2)
dll.print_ll()