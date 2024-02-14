class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def _insert(self, root, key):
    if root is None:
      return Node(key)
    else:
      if root.val < key:
        root.right = self._insert(root.right, key)
      else:
        root.left = self._insert(root.left, key)
    return root
  
  def inorder(self):
    self._inorder(self.root)
    print()

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      print(root.val, end=" ")
      self._inorder(root.right)

tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
tree.inorder()


