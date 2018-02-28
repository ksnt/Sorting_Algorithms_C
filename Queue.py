# Queue
# FIFO

class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop() # pop an element in the last element in the queue

	def size(self):
		return len(self.items)


q = Queue()
q.enqueue("first element")
q.enqueue("second element")
q.enqueue(3)
print("First dequeue result is: ", q.dequeue())
print("Now in the queue, there are these elements:", q.items)
print("Second dequeue result is: ", q.dequeue())
