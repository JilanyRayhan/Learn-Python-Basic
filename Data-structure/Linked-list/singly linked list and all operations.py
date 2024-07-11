class Node:
  def __init__(self,data): #we only took object and data  as a parameter,cause next is not a parameter or input
    self.data = data
    self.next = None

class Linked_list:
  def __init__(self):
    self.head = None

  def find_length(self):
    currentNode = self.head
    length = 0
    while currentNode is not None:
      length += 1
      currentNode = currentNode.next
    return length 

  def islistempty(self):
    if self.head is None:
      return True
    else:
      return False

  def insertat(self,newNode, position): #allows to enter a  node in a particular index position,from head to end,anywhere
    if position < 0 or position > self.find_length():
      print("invalid position")
      return
    elif position == 0:
      self.insertathead(newNode)
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

  def insertathead(self,newNode):    # allows a particular node to enter in the head of the Linked list without breaking the connection with other nodes   
    tempoNode = self.head
    self.head = newNode
    newNode.next = tempoNode
    del tempoNode

  def insertatend(self,newnode):     # allows nodes to enter at the end of the linked list
    if self.head is None:
      self.head = newnode                  #head = newnode
    else:
      lastnode = self.head
      while True:
        if lastnode.next is None:
          break
        lastnode = lastnode.next
      lastnode.next = newnode              #next = newnode

  def deletehead(self):
    if self.islistempty() is False:
      currentNode = self.head
      self.head = self.head.next
      del currentNode
    else:
      print("linked list is empty. delete failed.")

  def deleteatend(self):
    lastNode = self.head
    while lastNode.next is not None:
      previousNode = lastNode
      lastNode = lastNode.next
    previousNode.next = None 

  def deleteat(self,position):
    if position < 0 or position > self.find_length():
      print("invelid position")
      return
    if self.islistempty is False:
      if position == 0:
        self.deletehead()
        return
        currentNode = self.head
        current_position = 0
        while True:
          if current_position == position:
            previousNode.next = currentNode.next
            currentNode = None
            break
          previousNode = currentNode
          currentNode = currentNode.next
          current_position += 1

  def print_list(self):
    currentnode = self.head
    while True:
      if currentnode is None:
        break
      print(currentnode.data)
      currentnode = currentnode.next

firstnode = Node("bob")
linkedlist = Linked_list()
linkedlist.insertatend(firstnode)
secondnode = Node('sham')
linkedlist.insertatend(secondnode)
thirdnode = Node('harry')
linkedlist.insertatend(thirdnode)
fourthnode = Node('robin')
linkedlist.insertatend(fourthnode)
fifthnode = Node("ron")
linkedlist.insertathead(fifthnode)
sixthnode = Node("kate")
linkedlist.insertat(sixthnode,3)
linkedlist.deleteatend()
linkedlist.deleteat(0)
linkedlist.deletehead()
linkedlist.islistempty()
linkedlist.print_list()

 #explain the code using specific numbers to illustrate 