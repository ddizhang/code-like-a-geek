# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # left son depth + right son depth
        # loop through all nodes
        # post order (left - right - root)
        
        self.max_length = 0
        _ = self.findDepth(root)
        return self.max_length
        
    # this helper function is to recursively loop through all nodes
    # find the depth of each node, and update longest path when eligible
    def findDepth(self, node):
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 0
        
        if node.left:
            left_depth = self.findDepth(node.left) + 1
        else:
            left_depth = 0
        
        if node.right:
            right_depth = self.findDepth(node.right) + 1
        else:
            right_depth = 0
            
        node_diameter = left_depth + right_depth
        if node_diameter > self.max_length:
            self.max_length = node_diameter
        
        return max(left_depth, right_depth)
        
        