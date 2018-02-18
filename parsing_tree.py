# class BinaryTree:
# 	def __init__(self, rootVal):
# 		self.root = rootVal
# 		self.leftChild = None
# 		self.rightChild = None


def parsingTree(exp):

	res = BinaryTree(None)
	curr = res
	tree_stack = []

	for char in exp:

		if char == '(':
			curr.leftChild = BinaryTree(None)
			tree_stack.append(curr)
			curr = curr.leftChild

		if char in '0123456789':
			curr.root = char
			curr = tree_stack.pop()

		if char in '+-*/':
			curr.root = char
			tree_stack.append(curr)
			curr.rightChild = BinaryTree(None)
			curr = curr.rightChild

		if char == ')':
			curr = tree_stack.pop()



def evaluate(parse_tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    leftC = parse_tree.leftChild
    rightC = parse_tree.rightChild

    if leftC and rightC:
    	fn = opers[parse_tree.rootVal]
    	return fn(evaluate(leftC), evaluate(rightC))
    else: 
    	return parse_tree.rootVal






