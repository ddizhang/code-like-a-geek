# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # walk down from the root as long as both p and q are in the same subtree
        # (p and q are both smaller than or greater than the subtree root value)
        
        node = root
        ancestor = None
        
        while node:
            if node.val < p.val and node.val < q.val:
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else:
                break
        
        return node
    
    #recursive
    def lowestCommonAncestor(self, root, p, q):
        next = p.val < root.val > q.val and root.left or \
               p.val > root.val < q.val and root.right
        return self.lowestCommonAncestor(next, p, q) if next else root