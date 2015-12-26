"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Example
Given graph:

A----->B----->C
 \     |
  \    |
   \   |
    \  v
     ->D----->E
for s = B and t = E, return true

for s = D and t = C, return false
"""

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        from collections import deque
        if s is t:
            return True
        queue, visited = deque([s]), set([s])
        while queue:
            next_level = deque([])
            while queue:
                node = queue.popleft()
                for neighbor in node.neighbors:
                    if neighbor is t:
                        return True
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_level.append(neighbor)
            queue = next_level
        return False

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        if s is t:
            return True
        self.visited = set([s])

        def dfs(v):
            self.visited.add(v)
            for neighbor in v.neighbors:
                if neighbor in self.visited:
                    continue
                if neighbor is t:
                    return True
                if dfs(neighbor):
                    return True
            return False
        return dfs(s)
