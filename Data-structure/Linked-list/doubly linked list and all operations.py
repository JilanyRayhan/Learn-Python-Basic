class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def list_length(self):
    currentNode = self.head
    length = 0
    while currentNode:
      length += 1
      currentNode = currentNode.next
    return length

  def insertAthead(self,newNode):
      if self.head:
          newNode.next = self.head
          self.head.prev = newNode
      self.head = newNode

  def insertAt(self,newNode,position):
    if position < 0 or position > self.list_length():
      print("invalid position")
      return
    if position == 0:
      self.insertAthead(newNode)
      return
    currentNode = self.head
    current_position = 0
    while True:
      if current_position == position:
        previousNode.next = newNode
        newNode.prev = previousNode
        newNode.next = currentNode
        currentNode.prev = newNode
        break
      previousNode = currentNode
      currentNode = currentNode.next
      current_position += 1

  def insertAtend(self,newNode):
    if self.head is None:
      self.head = newNode
    else:
      currentNode = self.head
      while currentNode.next:
          currentNode = currentNode.next
      currentNode.next = newNode
      newNode.prev = currentNode

  def deleteAthead(self):
    if self.head is None:
      return
    self.head = self.head.next
    if self.head is not None:
      self.head.prev = None

  #revise this delete at function with chatgpt. and discover something new
  def deleteAt(self,position):
    if self.head is None:
      print("the linked list is empty. no nodes to delete.")
      return
    if position < 0 or position >= self.list_length():
      print("invalid position.")
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
      print("out of bound.")
    currentNode.prev.next = currentNode.next
    if currentNode.next:
      currentNode.next.prev = currentNode.prev
    del currentNode


  def deleteAtend(self):
    if self.head is None:
      print("the linked list is empty. no element to delete.")
      return
    currentNode = self.head
    if currentNode.next is None:
      currentNode = None
    else:
      while currentNode.next:
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

node1 = Node(10)
linkedlist = LinkedList()
linkedlist.insertAtend(node1)
node2 = Node(20)
linkedlist.insertAtend(node2)
node3 = Node(30)
linkedlist.insertAtend(node3)
node4 = Node(5)
linkedlist.insertAthead(node4)
node5 = Node(25)
linkedlist.insertAt(node5,3)
linkedlist.deleteAtend()
linkedlist.deleteAthead()
linkedlist.deleteAt(2)
linkedlist.print_ll()