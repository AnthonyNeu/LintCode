"""
Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. 
(a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

Given graph:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        m, self.visited = len(nodes), {node:False for node in nodes}
        result = []
        
        def bfs(node):
            from collections import deque
            queue = deque([node])
            self.visited[node] = True
            cc = []
            while queue:
                u = queue.popleft()
                cc.append(u.label)
                for v in u.neighbors:
                    if not self.visited[v]:
                        self.visited[v] = True
                        queue.append(v)
            cc.sort()
            result.append(cc)
        for node in nodes:
            if self.visited[node] is False:
                bfs(node)
        return result
