  class Node:
    def __init__(self,data):
      self.data = data
      self.next = None
      self.prev = None

  class cd_linked_list:
    def __init__(self):
      self.head = None
      self.tail = None

    def isEmpty(self):
      return self.head is None

    def length(self):
      currentNode = self.head
      count = 0
      while currentNode is not None:
          count += 1
          currentNode = currentNode.next
          if currentNode == self.head:
              break
      return count

    def insertAthead(self,data):
      newNode = Node(data)
      if self.isEmpty():
        self.head = newNode
        self.head.next = self.head
        self.head.prev = self.head
        self.tail = newNode
      else:
        newNode.next = self.head
        self.head.prev = newNode
        currentNode = self.head
        while currentNode.next != self.head:
          currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode
        self.head = newNode
        self.tail = currentNode

    def insertAt(self,data,position):
      newNode = Node(data)
      if self.isEmpty():
        print("the linked list is empty.")
        return
      if position < 0 or position > self.length():
        print("invalid position.")
        return
      if position == 0:
        self.insertAthead(newNode)
        return
      currentNode = self.head
      current_position = 0
      while current_position < position:
        current_position += 1
        currentNode = currentNode.next
      currentNode.prev.next = newNode
      newNode.prev = currentNode.prev
      newNode.next = currentNode
      currentNode.prev = newNode

    def insertAttail(self,data):
      newNode = Node(data)
      if not self.head:
        self.head = newNode
        self.head.next = self.head
        self.head.prev = self.head
        #when we have only one node in a linked list. it is both the head and the tail
        self.tail = newNode 
        return
      currentNode = self.head
      while currentNode.next != self.head:
        currentNode = currentNode.next
      currentNode.next = newNode
      newNode.prev = currentNode
      newNode.next = self.head
      self.head.prev = newNode

      self.tail = newNode

    def deleteAthead(self):
      if self.isEmpty():
        print("the linked list is empty.")
        return
      if self.head.next == self.head:
        self.head = None
        return
      currentNode = self.head
      while currentNode.next != self.head:
        currentNode = currentNode.next
      currentNode.next = self.head.next
      self.head.next.prev = currentNode
      self.head = self.head.next

    def deleteAt(self,position):
      if self.isEmpty():
        print("the linked list is empty, nothing to delete.")
        return
      if position < 0 or position > self.length():
        print("invalid position")
        return
      if position == 0:
        self.deleteAthead()
        return
      currentNode = self.head
      current_position = 0
      while current_position < position:
        currentNode = currentNode.next
        current_position += 1
      currentNode.prev.next = currentNode.next
      currentNode.next.prev = currentNode.prev
      if currentNode.next == self.head:
        currentNode.prev.next = self.head
        self.head.prev = currentNode.prev

    def deleteAttail(self):
      if self.isEmpty():
        print("the list is empty, nothing to delete.")
        return
      if self.head.next == self.head:
        self.head = None
        return
      currentNode = self.head
      while currentNode.next != self.head:
        currentNode = currentNode.next
      currentNode.prev.next = self.head
      self.head.prev = currentNode.prev
      # Note: Avoid explicitly deleting nodes in Python unless you're managing memory at a lower level,
      # as Python's garbage collector will take care of deallocating memory.
      del currentNode

    def print_cdll(self):
      currentNode = self.head
      while True:
        if currentNode.next == self.head:
          break
        print(currentNode.data)
        currentNode = currentNode.next
      print(currentNode.data)
  cdll = cd_linked_list()
  cdll.insertAttail(20)
  cdll.insertAttail(30)
  cdll.insertAttail(40)
  cdll.insertAttail(50)
  cdll.insertAttail(60)
  cdll.insertAttail(70)
  cdll.insertAttail(80)
  cdll.insertAthead(10)
  cdll.insertAt(80,7)
  cdll.insertAt(60,5)
  cdll.deleteAthead()
  cdll.deleteAttail()
  cdll.deleteAt(5)
  cdll.print_cdll()