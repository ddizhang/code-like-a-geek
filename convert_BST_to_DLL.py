"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # maintain a queue for insertion
        # insert a node to it's proper place
        
        if not root:
            return None
        
        queue = [[root, None, None]]
        self.head = root
        
        while queue:
            node, is_child, parent = queue.pop(0)
            if node:
                # print('\n')
                # print('node.val:'+str(node.val))
                queue.append([node.left, 'left', node])
                # if node.left: 
                #     print('add node:' + str(node.left.val) + 'to queue')
                # else: 
                #     print('left node is None')
                
                queue.append([node.right, 'right', node])
                # if node.right: 
                #     print('add node:' + str(node.right.val) + 'to queue')
                # else:
                #     print('right node is None')
                self.toList(node, is_child, parent)
        
        return self.head
    
    # helper, insert a given node into the list
    def toList(self, node, is_child, parent):
        
        if not node:
            # print('node is None')
            return None
        
        # print('\n')
        # print('converting node '+ str(node.val))
        # if current node is the left child of parent:
        if is_child == 'left':
            node.left = parent.left
            parent.left.right = node
            node.right = parent
            parent.left = node
            # head pointer
            if node.val < self.head.val:
                self.head = node
                
        # if current node is right child:
        elif is_child == 'right':
            node.right = parent.right
            parent.right.left = node
            node.left = parent
            parent.right = node
        
        # if current node is root:
        else:
            node.right = node
            node.left = node
        
        # print('converting finished.')
        # if node.left:
        #     print('node.left:' + str(node.left.val))
        # if node.right:
        #     print('node.right:' + str(node.right.val))
        # if parent and parent.left:
        #     print('parnet.left: ' + str(parent.left.val))
        # if parent and parent.right:
        #     print('parent.right: '+ str(parent.right.val))
        
        
        
        
        