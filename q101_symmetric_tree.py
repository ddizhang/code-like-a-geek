# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # pre-order traverse left tree, put into a list
        # mirrored pre-order traverse right tree, put into a list
        # compare the two lists
        # note: if not comparing left.val and right.val, won't pass [1,2,3,3,null,2,null]
        
        if root is None:
            return True
        
        if root.left is None or root.right is None:
            if not root.left and not root.right:
                return True
            else:
                return False
        
        if root.left.val != root.right.val:
            return False
        
        left_list, right_list = [], []
        self.left_root_right(root.left, left_list)
        self.right_root_left(root.right, right_list)
        
        print(left_list)
        print(right_list)
        
        if len(left_list) != len(right_list):
            return False
        
        for i in range(len(left_list)):
            if left_list[i] != right_list[i]:
                return False
        return True
    
    def left_root_right(self, node, answer):
        if not node:
            answer.append(None)
        else:
            self.left_root_right(node.left, answer)
            answer.append(node.val)
            self.left_root_right(node.right, answer)
            
    def right_root_left(self, node, answer):
        if not node:
            answer.append(None)
        else:
            self.right_root_left(node.right, answer)
            answer.append(node.val)
            self.right_root_left(node.left, answer)
            
    
    # if two trees are mirror images:
    # node1.left is mirror to node2.right
    # node1.right is mirror to node2.left
        
    def isSymmetric(self, root):
        return self.isMirror(root, root)
    
    def isMirror(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        
        boolean = n1.val == n2.val and\
                  self.isMirror(n1.left, n2.right) and\
                  self.isMirror(n1.right, n2.left)
        return boolean
        