class BinaryHeap:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	def percUp(self, i):
		parent_pos = i//2
		while parent_pos > 0 and self.heap[i] < self.heap[parent_pos]:
			temp = self.heap[i]
			self.heap[i] = self.heap[parent_pos]
			self.heap[i] = temp

			i = parent_pos
			parent_pos = i//2

	def insert(self, val):
		self.heap.append(val)
		self.size = self.size + 1
		self.percUp(self.size)


	def percDown(self, i):

		while i*2 <= len(self.size):
			minchild_pos = minChild(i)
			if self.heap[i] > self.heap[minchild_pos]:
				temp = self.heap[i]
				self.heap[i] = self.heap[minchild_pos]
				self.heap[minchild_pos] = temp
			i = minchild_pos

				
	def minChild(self, i):
		if i*2+1 > self.size:
			return i*2
		else:
			if self.heap[i*2+1] > self.heap[i*2]:
				return i*2
			else:
				return i*2+1

	def delMin(self):
		self.heap[1] = self.heap.pop()
		self.size -= 1
		self.percDown(1)


