# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # can't just compare the two child node values with parent value
    # right child's left child should also be larger than grandpa
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.validBSTnode(root, None, None)
    
    def validBSTnode(self, node, greater_than_value, less_than_value):
        
#         print('\n')
#         print('node.val: '+str(node.val))
#         print('greater_than_value'+str(greater_than_value))
#         print('less_than_value'+str(less_than_value))
        
        if greater_than_value is not None and node.val <= greater_than_value:
            return False
        if less_than_value is not None and node.val >= less_than_value:
            return False
        
        validBST = True

        # child node is inheriting parent's restrict
        if node.left:           
            validBST = validBST and self.validBSTnode(node.left, greater_than_value, node.val)
                
        if node.right:            
            validBST = validBST and self.validBSTnode(node.right, node.val, less_than_value)
            
        return validBST
            
        
            