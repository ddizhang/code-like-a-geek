# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # iteratively
    def searchBST1(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val < val:
                node = node.right
            else:
                node = node.left
        
        return None
    
    # recursively
    def searchBST(self, root, val):
        return self.searchBST_helper(root, val)
    
    def searchBST_helper(self, node, val):
        if not node:
            result = None
        
        #print('node.val:'+ str(node.val))
        elif node.val == val:
            result = node
        
        elif node.val < val:
            result = self.searchBST_helper(node.right, val)
        else:
            result = self.searchBST_helper(node.left, val)
        
        return result