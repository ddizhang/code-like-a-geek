# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # top-down        
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        answer = [0]
        self.maxDepth_helper(root, 1, answer)
        return answer[0]
        
    def maxDepth_helper(self, node, depth, answer):
        
        # if node is not None: print(str(node.val))
        if node is None:
            return None
        
        # is leave
        if node.left is None and node.right is None:
            answer[0] = max(answer[0], depth)
        
        self.maxDepth_helper(node.left, depth+1, answer)
        self.maxDepth_helper(node.right, depth+1, answer)
        
        
    # bottom-up
    def maxDepth(self, root):
        
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth)+1

        
        
            
        