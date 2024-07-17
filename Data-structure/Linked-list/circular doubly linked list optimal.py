class Node:
  def __init__(self, data):
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
      if self.isEmpty():
          return 0
      current = self.head
      count = 0
      while True:
          count += 1
          current = current.next
          if current == self.head:
              break
      return count

  def insertAthead(self, data):
      new_node = Node(data)
      if self.isEmpty():
          self.head = new_node
          self.tail = new_node
          new_node.next = new_node
          new_node.prev = new_node
      else:
          new_node.next = self.head
          new_node.prev = self.tail
          self.head.prev = new_node
          self.tail.next = new_node
          self.head = new_node

  def insertAttail(self, data):
      new_node = Node(data)
      if self.isEmpty():
          self.insertAthead(data)
      else:
          new_node.next = self.head
          new_node.prev = self.tail
          self.tail.next = new_node
          self.head.prev = new_node
          self.tail = new_node

  def insertAt(self, data, position):
      if position < 0 or position > self.length():
          print("Invalid position.")
          return
      if position == 0:
          self.insertAthead(data)
          return
      if position == self.length():
          self.insertAttail(data)
          return

      new_node = Node(data)
      current = self.head
      count = 0
      while count < position:
          current = current.next
          count += 1
      new_node.next = current
      new_node.prev = current.prev
      current.prev.next = new_node
      current.prev = new_node

  def deleteAthead(self):
      if self.isEmpty():
          print("The linked list is empty.")
          return
      if self.head == self.tail:
          self.head = None
          self.tail = None
      else:
          self.head = self.head.next
          self.head.prev = self.tail
          self.tail.next = self.head

  def deleteAttail(self):
      if self.isEmpty():
          print("The linked list is empty.")
          return
      if self.head == self.tail:
          self.head = None
          self.tail = None
      else:
          self.tail = self.tail.prev
          self.tail.next = self.head
          self.head.prev = self.tail

  def deleteAt(self, position):
      if self.isEmpty():
          print("The linked list is empty.")
          return
      if position < 0 or position >= self.length():
          print("Invalid position.")
          return
      if position == 0:
          self.deleteAthead()
          return
      if position == self.length() - 1:
          self.deleteAttail()
          return

      current = self.head
      count = 0
      while count < position:
          current = current.next
          count += 1
      current.prev.next = current.next
      current.next.prev = current.prev

  def print_cdll(self):
      if self.isEmpty():
          print("The linked list is empty.")
          return
      current = self.head
      while True:
          print(current.data)
          current = current.next
          if current == self.head:
              break
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