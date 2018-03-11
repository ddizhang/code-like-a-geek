# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # there's no need to write the helper..
        return self.lca_helper(root, p, q)
    
    #if left and child borh contains p/q (in this case, a child can only contain one deserved node): return root
    #if only one child contains p/q (the child has to contain both of them!) then return the child
    def lca_helper(self, node, p, q):
        
        if node in (None, p, q):
            return node
        
        left = self.lca_helper(node.left, p, q)
        right = self.lca_helper(node.right, p, q)
        
        if left and right:
            return node
        else:
            return left or right
        
        
        
    # this is post-order traversal
    # can write it with a stack (I believe?)
    def lowestCommonAncestor(self, root, p, q):
        
        stack = []
        # whether node contains one child
        node_dict = {}
        stack.append([root, 0])
        
        while stack:
            node, visited = stack.pop()
            pp = node.val if node else 'None'
            print('Node:' + str(pp))
            
            if visited == 1:
                # if left and right both contains one child: then node is LCA
                if node:
                    left = node_dict[node.left] if node.left in node_dict else None
                    right = node_dict[node.right] if node.right in node_dict else None
                    node_val = node_dict[node]
                    if (left and right) or (left and node_val) or (right and node_val):
                        return node
                    # print('node visited = 1.')
                    # print('left: ' + str(left))
                    # print('right: ' + str(right))
                    # print('node_val:' + str(node_val))
                    node_dict[node] = 1 if left or right or node_val else 0

            else:
                if node:
                    if node in (p, q):
                        node_dict[node] = 1
                    else:
                        node_dict[node] = 0
                        
                    stack.append([node, 1])
                    stack.append([node.left, 0])
                    stack.append([node.right, 0])
                
        return False
    
    