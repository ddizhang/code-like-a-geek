# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths1(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        
        left_path = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        right_path = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        
        return left_path + right_path
    
    
    def binaryTreePaths(self,root):
        if not root:
            return []
        stack = [[root, str(root.val)]]
        res = []
        
        while stack:
            node, path = stack.pop()
            if node: 
                # print('node:' + str(node.val))
                # print('path:' + path)
                # print('\n')
                if not node.left and not node.right:
                    res.append(path)
                else:
                    if node.right:
                        stack.append([node.right, path + '->' + str(node.right.val)])
                    if node.left:
                        stack.append([node.left, path + '->' + str(node.left.val)])
        return res