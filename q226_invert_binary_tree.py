

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        new_root = TreeNode(root.val)
        new_root.left = self.invertTree(root.right)
        new_root.right = self.invertTree(root.left)
        
        return new_root
