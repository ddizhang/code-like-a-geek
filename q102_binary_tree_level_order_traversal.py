# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder0(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # below is assuming a complete binary tree, which is not always the case!
        if root is None:
            return []
        
        queue = [root]
        result = [[]]
        lev = 1
        node_count = 0
        while queue:
            curr_node = queue.pop(0)
            node_count += 1
            
            if curr_node:
                queue.append(curr_node.left)
                queue.append(curr_node.right)
                
                if node_count >= 2**lev:
                    result.append([])
                    lev += 1
                result[lev-1].append(curr_node.val)
            
        return result
        
    # this one works!
    def levelOrder(self, root):
        queue = [[root, 0]]
        result = []

        while queue:
            curr_node, level = queue.pop(0)
            if curr_node:                
                queue.append([curr_node.left, level+1])
                queue.append([curr_node.right, level+1])
                 
                if len(result) < level+1:
                    result.append([])
                
                result[level].append(curr_node.val)
        
        return result
                 

                
                 
                 
        