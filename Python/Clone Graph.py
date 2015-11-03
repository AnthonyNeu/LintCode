"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution1:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node
        
        def dfs(start):
            if start in self.dict:
                return self.dict[start]
            new_node = UndirectedGraphNode(start.label)
            self.dict[start] = new_node 
            for neighbor in start.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)

class Solution2:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node
        cloned_node = UndirectedGraphNode(node.label)
        self.dict[node], queue = cloned_node, [node]
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in self.dict:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    self.dict[neighbor] = cloned_neighbor
                    queue.append(neighbor)
                self.dict[current].neighbors.append(self.dict[neighbor])
        return cloned_node

