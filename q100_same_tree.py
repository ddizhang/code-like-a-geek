# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # similar to 'mirror tree' 
        # recursively compare two trees nodes:
        # n1.val == n2.val?
        # n1.left == n2.left?
        # n1.right == n2.right?
        