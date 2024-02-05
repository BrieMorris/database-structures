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
    s11 = SinglyLinkedList()
    s11.add.node(1)
    s11.add.node(2)
    s11.add.node(3)
    s11.display()


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
      new_node.prev = current_node
  
  def display_forward(self):
    current_node + self.head
    while current_node:
      print(current_node.data, end="<->")
      current_node= current_node.nest
    print("None")

  def display_backward(self):
    current_node = self.hand
    while current_node.next:
      current_node = current_node.next
    while current_node:
      print(current_node.data, end="<->")
      cureent_node = current_node.prev
    print("None")

# Instantiate a new Doubly linked list
 d11 =DoublyLinkedList()   

# add nodes to the list
d11.add_node(1)
d11.add_node(2)
d11.add_node(3)
    
# Display the list in forward and backward direction
d11.display_forward
d11.display_backward
