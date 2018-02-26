class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0


	def _put(self, key, val, curr_node):

		if key < curr_node.key:
			if curr_node.leftChild is not None:
				self._put(key, val, curr_node.leftChild)
			else:
				curr_node.leftChild = TreeNode(key, val, parent = curr_node)
		else:
			if curr_node.rightChild is not None:
				self._put(key, val, curr_node.rightChild)
			else:
				curr_node.rightChild = TreeNode(key, val, parent = curr_node)


	def put(self, key, val):

		curr_node = self.root
		if not self.root:
			self.root = TreeNode(key, val)
		else:
			self._put(key, val, curr_node)

		self.size = self.size + 1


	def __setitem__(self, k, v):
		self.put(k, v)


	def get(self, key):

		curr_node = self.root
		return self._get(key, curr_node).val


	def _get(self, key, curr_node):

		if key = curr_node.key:
			return curr_node
		#search left child	
		if key < curr_node.key:
			if curr_node.leftChild is not None:
				self._get(key, curr_node.leftChild)
			else:
				return None

		if key > curr_node.key:
			if curr_node.rightChild is not None:
				self._get(key, curr_node.rightChild)
			else:
				return None

	def __getitem__(self, k):
		self.get(k)


	def delete(self, key):

		node_to_del = self._get(key, self.root)

		if self.size == 1 and key = self.root.key:
			self.root = None
			self.size = 0
			return None

		if node_to_del:
			self.remove(node_to_del)
			self.size -= 1

		else:
			raise KeyError('Error, key not in tree')




	def __delitem(self, item):
		self.delete(item)

	def remove(self, node_to_del):

		# if it has no child:
		if not node_to_del.leftChild and not node_to_del.rightChild:
			#delete it 
			if node_to_del.parent and node_to_del.is_left_child:
				node_to_del.parent.leftChild = None
			if node_to_del.parent and node_to_del.is_right_child:
				node_to_del.parent.rightChild = None

		# if it has one child: child take its place
		if node_to_del.has_one_child():
			
			node_to_del_child = node_to_del.leftChild or node_to_del.rightChild
			# if it's a left child
			if node_to_del.parent and node_to_del.is_left_child:
				node_to_del.parent.leftChild = node_to_del_child
				node_to_del_child.parent = node_to_del.parent
			# if it's a right child
			if node_to_del.parent and node_to_del.is_right_child:
				node_to_del.parent.rightChild = node_to_del_child
				node_to_del_child.parent = node_to_del.parent

		# if it has both children: find the leftmost right child
		if node_to_del.has_both_children():

			successor = node_to_del.leftChild
			while successor.leftChild:
				successor = node_to_del.leftChild

		if node_to_del.parent and node_to_del.is_left_child:
			node_to_del.parent.leftChild = successor
			successor.parent = node_to_del.parent
		# if it's a right child
		if node_to_del.parent and node_to_del.is_right_child:
			node_to_del.parent.rightChild = successor
			successor.parent = node_to_del.parenttChild









class TreeNode:

	def __init__(self, key, val, leftChild = None, rightChild = None, parent = None):
		self.key = key
		self.val = val
		self.leftChild = leftChild
		self.rightChild = rightChild
		self.parent = parent

	def is_left_child(self):
		parent = self.parent
		return parent and parent.leftChild == self

	def is_right_child(self):
		parnt = self.parent
		return parent and parent.rightChild == self


	def has_one_child(self):

		if self.leftChild and self.rightChild:
			return False
		else:
			return self.leftChild or self.rightChild

	def has_both_children(self):
		return self.leftChild and self.rightChild






	









