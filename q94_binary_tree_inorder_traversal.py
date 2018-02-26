# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # left -> root -> right
        # iteratively
        
        result, stack = [], []
        curr_node = root
        
        while stack or curr_node:
            if curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                result.append(curr_node.val)
                curr_node = curr_node.right
            
        return result