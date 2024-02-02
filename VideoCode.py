class Node:
  def _init_(self, data):
   self.data = data
   self.nest = None

class SinglyLinkedList:
  def _init_(self):
    self.head = None
  
  def add_node(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next:
        current_node = current_node.next
      current_node.next = new_node

# display operation lets us know that our add_node operation is working 
  def display(self):
    current_node = self.head
    while current_node:
      print(current_node.data, ends=" ->")
      current_node = current_node.next
    print("None")

# Example Usage:
    sll = SinglyLinkedList()
    sll.add.node(1)
    sll.add.node(2)
    sll.add.node(3)
    sll.display()


class DoublyNode:
  def _init_(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def _init_(self):
    self.head = None
  
  def add_node(self, data):
    new_node = DoublyNode(data)
    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next:
        current_node = current_node.next
      current_node = current_node.next
      new_node.prev = current_node
  
  def display_forward(self):
    current_node + self.head
    while current_node:
      print(current_node.data, end="<->")
      current_node= current_node.nest
    print("None")


