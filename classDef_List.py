class Node:
	def __init__(self, initData):
		self.val = initData
		self.next = None

	def getData(self):
		return self.val

	def setData(self, val):
		self.val = val

	def getNext(self):
		return self.next

	def setNext(self, nextNode):
		self.next = nextNode


class unorderedList:
	def __init__(self):
		self.head = None #head is a listNode

	def isEmpty(self):
		return self.head == None

	def addNode(self, newNodeVal):
		newNode = Node(newNodeVal)
		newNode.setNext(self.head)
		self.head = newNode

	def size(self):
		i = 0
		ptr = self.head

		while ptr:
			i = i + 1
			ptr = ptr.next

		return i

	def delete(self, val):
		ptr = self.head
		prev = None

		while ptr and ptr.val != val:
			prev = ptr
			ptr = ptr.next

		if prev == None:
			self.head = ptr.
		else:
			prev.next = ptr.next















