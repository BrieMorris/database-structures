# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None  

#     def add_node(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node
            
#     def display(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")
    
#     def reverse(self):
#         reversed_part = None
#         current = self.head
#         while current:
#             future = current.next
#             current.next = reversed_part
#             reversed_part = current
#             current = future
        
#         return reversed_part


# # Example usage:
# sll = SinglyLinkedList()
# sll.add_node(1)
# sll.add_node(2)
# sll.add_node(3)
# sll.display()
# sll.reverse()
# sll.display()

class DoublyNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
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
    current_node = self.head
    while current_node:
      print(current_node.data, end=" <-> ")
      current_node = current_node.next
    print("None")

  def display_backward(self):
    current_node = self.head
    while current_node.next:
      current_node = current_node.next
    while current_node:
      print(current_node.data, end=" <-> ")
      current_node = current_node.prev
    print("None")

# Instantiate a new Doubly linked list
dll = DoublyLinkedList()   

# add nodes to the list
dll.add_node(1)
dll.add_node(2)
dll.add_node(3)
    
# Display the list in forward and backward direction
dll.display_forward()
dll.display_backward()
