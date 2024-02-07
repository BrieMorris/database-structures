class Stack:
  def __init__(self):
    self.stack = []

  def is_empty(self):
    return len(self.stack) == 0
  
  def size(self):
    return len(self.stack)
  
  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if not self.is_empty():
      return self.stack.pop()
    else:
      return "Stack is empty"
  
  def peek(self):
    if not self.is_empty():
      return self.stack[-1]
    else:
      return "stack is empty"
    
# Instatiaate the stack class
my_stack = Stack()

# Push some elements 
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# pop an element 
print(my_stack.pop()) # output shou be 3

# peek at the top 
print(my_stack.peek()) # output 2

#check the size
print(my_stack.size()) # output 2
    

class Queue:
  def __init__(self):
    self.queue = []

  def is_empty(self):
    return len(self.queue) == 0
  
  def size(self):
    return len(self.queue)
  
  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if not self.is_empty():
      return self.queue.pop(0)
    else:
      return "Queue is empty"
    
  def front(self):
    if not self.is_empty():
      return self.queue[0]
    else:
      return "Queue is empty" 
    
#example usuage 
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue.dequeue) # print 1
print(my_queue.front()) # print 2
my_queue.enqueue(4)
print(my_queue.size()) # 3

   