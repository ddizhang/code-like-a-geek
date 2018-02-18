class BinaryTree:
	def __init__(self, rootVal):
		self.root = rootVal
		self.leftChild = None
		self.rightChild = None



# tree traverse

def preorder(tree):

	if tree:
		print(tree.root)
		preorder(tree.leftChild)
		preorder(tree.rightChild)