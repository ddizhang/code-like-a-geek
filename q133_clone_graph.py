# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    
    # time limit exceeded..
    def cloneGraph1(self, node):
        
        if not node:
            return None
        node_dict = {}
        
        new_node = UndirectedGraphNode(node.label)
        node_dict[node.label] = new_node
        
        for neighbor in node.neighbors:
            # if the node is already in the graph
            if neighbor.label in node_dict:
                new_node.neighbors.append(node_dict[neighbor.label])
            else:
                new_node.neighbors.append(self.cloneGraph(neighbor))
        
        return new_node
    
    
    # now this works
    def cloneGraph2(self, node):
        
        self.node_dict = {}
        new_node = self.cloneNode(node)
        return new_node
        
    
    def cloneNode(self, node):
        
        if not node:
            return None
        
        # if the node is already in the cloned graph:
        if node.label in self.node_dict:
            return self.node_dict[node.label]
        
        new_node = UndirectedGraphNode(node.label)
        self.node_dict[node.label] = new_node
        
        for neighbor in node.neighbors:
                new_node.neighbors.append(self.cloneNode(neighbor))
        
        return new_node
    
    
    # try BFS and DFS iterative?
    
    
    # in this case, using BFS and DFS iterative have exactly the same syntax
    # just that the former use a queue and latter use a stack
    # construct the node first
    # when it's time to visit the node, add in its neighbors
    def cloneGraph(self, node):
        if not node:
            return None
        node_dict = {}
        
        new_root = UndirectedGraphNode(node.label)
        node_dict[new_root.label] = new_root
        # put in the node in ORIGINAL GRAPH into stack
        # because we need to iterate over all its neighbors later
        stack = [node]
        
        while stack:
            # DFS
            curr_orig_node = stack.pop()
            # BFS
            # curr_orig_node = stack.pop(0)
                          
            curr_new_node = node_dict[curr_orig_node.label]
            for neighbor in curr_orig_node.neighbors:
                if neighbor.label not in node_dict:
                    node_dict[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                curr_new_node.neighbors.append(node_dict[neighbor.label])
        
        return new_root
            
        
    