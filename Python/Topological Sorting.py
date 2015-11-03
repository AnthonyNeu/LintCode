"""
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.
"""

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# BFS
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        result, in_degree = [], {}
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in in_degree:
                    in_degree[neighbor] += 1
                else:
                    in_degree[neighbor] = 1
        queue = []
        for node in graph:
            if node not in in_degree:
                queue.append(node)
                result.append(node)
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(neighbor)
        return result

# DFS
# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        from sets import Set
        result, ancestors, nodes, scheduled = [], {}, Set(), Set()
        
        def find_ancestors_dfs(current):
            if current not in nodes:
                nodes.add(current)
                for neighbor in current.neighbors:
                    if neighbor not in ancestors:
                        ancestors[neighbor] = [current]
                    else:
                        ancestors[neighbor].append(current)
                    find_ancestors_dfs(neighbor)
        # find the ancestors of each node
        for node in graph:
            find_ancestors_dfs(node)
        
        def top_sort_dfs(start):
            if start not in scheduled:
                scheduled.add(start)
                if start in ancestors:
                    for ancestor in ancestors[start]:
                        top_sort_dfs(ancestor)
                result.append(start)
        # find the topological ordering by DFS
        for node in graph:
            top_sort_dfs(node)
        return result
