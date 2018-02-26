# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # recursively
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.preorder_helper(root, result)
        return result
    
    def preorder_helper(self, node, result):
        if node is not None:
            result.append(node.val)
            self.preorder_helper(node.left, result)
            self.preorder_helper(node.right, result)
    
    # iteratively
    # use a stack
    def preorderTraversal(self, root):
        result = []
        stack = [root]
        
        while stack:
            curr_node = stack.pop()
            if curr_node is not None:
                result.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)
        
        return result
    