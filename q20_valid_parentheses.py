def parChecker(string):

	left = '([{'
	right = ')]}'
	par_stack = []

	for char in string:
		# inserting new paranthesis opening
		if char in left:
			par_stack.append(char)

		# parenthesis closing
		elif char in right:
			# if parenthesis close without an open, or close with unmatched open:
			if len(par_stack) == 0 or char != right[left.index(par_stack[-1])]:
				return False
			else:
				par_stack.pop()

	return len(par_stack) == 0

