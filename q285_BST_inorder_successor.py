# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree.
# inorder: left - root - right
# smallest larger node


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # if it has a right child: 
        # leftmost of right child
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        
        # if the node doesn't have a right child:
        # search down from the root
        if not p.right:
            node = root
            successor = None
            
            while node and node.val != p.val:
                
                # if current node > p: see if can find a smaller one
                if node.val > p.val:
                    successor = node
                    # if there's no smaller one: current node is the successor
                    if not node.left or node.left.val == p.val:
                        break
                    
                    node = node.left
                
                # if current node < p: find a larger value
                elif node.val < p.val:
                    # if there's no larger node: no successor
                    if not node.right or node.right.val == p.val: 
                        break
                    node = node.right
            
            return successor
            