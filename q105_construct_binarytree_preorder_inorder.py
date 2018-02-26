# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder_dict = {val:idx for idx, val in enumerate(inorder)}
        
        if not preorder:
            return None
        
        root = self.build(0, 0, len(preorder))
        return root
    
    def build(self, preorder_start, inorder_start, tree_size):       
        
        # print('preorder_start: '+ str(preorder_start))
        # print('inorder_start: ' + str(inorder_start))
        # print('tree_size:' + str(tree_size))
        
        if tree_size == 0:
            node = None
            
        else:
            node_val = self.preorder[preorder_start]
            # print('node_val:'+str(node_val))

            if tree_size == 1:
                node = TreeNode(node_val)
            else:
                node_pos_inorder = self.inorder_dict[self.preorder[preorder_start]]
                left_tree_size = node_pos_inorder - inorder_start
                right_tree_size = tree_size - left_tree_size - 1

                # print('node_pos_inorder: '+ str(node_pos_inorder))
                # print('left_tree_size:' + str(left_tree_size))
                # print('right_tree_size:' + str(right_tree_size))
                # print('\n')
                
                node = TreeNode(node_val)
                node.left = self.build(preorder_start+1, node_pos_inorder-left_tree_size, left_tree_size)
                node.right = self.build(preorder_start+left_tree_size+1, node_pos_inorder+1, right_tree_size)

        return node

        