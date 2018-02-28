# Implementation of a stack ADT
# LIFO

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		""" Confirm whether a stack is empty or not"""
		return self.items == []

	def push(self,item):
		#self.items.append(item) # Add an item into items(list to store items)
		self.items.insert(0,item)

	def pop(self):
		#self.items.pop()
		return self.items.pop(0)

	def peek(self):
		""" return the last item (the item added at first) in items list"""
		#return self.items[len(self.items) - 1]
		return self.items[0]

	def size(self):
		""" return the length of items list"""
		return len(self.items)

m = Stack()
m.push("element1")
print("Now in the stack there are: ", m.items)
print("Length of the stack is: ",m.size())
print("Pop an element: ", m.pop())