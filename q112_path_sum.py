# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        return self.hasPathSumHelper(root, sum)
        
        
    def hasPathSumHelper(self, node, nodesum):
        
        # none: return false
        if not node:
            return False 
        
        # if it's a leaf
        if not node.left and not node.right:
            return node.val == nodesum
        
        # print('node.val:'+str(node.val))
        # print('childsumshouldbe:'+str(nodesum - node.val))
        # print('left'+str(self.hasPathSumHelper(node.left, nodesum-node.val)))
        # print('right'+str(self.hasPathSumHelper(node.right, nodesum-node.val)))
        
        # either left son has a path or right son has a path
        return self.hasPathSumHelper(node.left, nodesum-node.val) or\
               self.hasPathSumHelper(node.right, nodesum-node.val)
        
