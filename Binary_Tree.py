
class BinaryTree:
	def __init__(self,root):
		self.key = root
		self.left_child = None
		self.right_child = None

	def insert_left(self,new_node):
		# If left child is NOT there, then insert the new node as a root
		# If left chile is there, build a binary tree based on the new node first
		# Then,insert the original binary tree's left child into the new binary tree's left child
		# Finally, left child of the original binary tree is set to ledt child of the new binary tree
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def insert_right(self,new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.right_child = self.right_child
			self.right_child = t

	def get_right_child(self):
		return self.right_child

	def get_left_child(self):
		return self.left_child

	def set_root_val(self,obj):
		"""Set the value of rool"""
		self.key = obj

	def get_root_val(self):
		"""Get the value of root"""
		return self.key


r = BinaryTree('a')
print("The value of root is: ",r.get_root_val())
print("Left child is: ", r.get_left_child())
r.insert_left('b')
print("Now left child is:", r.get_left_child())
print("Now the value of left child is:", r.get_left_child().get_root_val())
r.insert_right('c')
print("Now left child is:",r.get_right_child())
print("Now the value of right child is:",r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print("Now the value of right child is:",r.get_right_child().get_root_val())