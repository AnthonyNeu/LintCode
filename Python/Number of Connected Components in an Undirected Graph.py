"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

# Union find
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents, result = [i for i in range(n)], n

        def find(i):
            if parents[i] == i:
                return i
            return find(parents[i])
        for i in range(len(edges)):
            x, y = find(edges[i][0]), find(edges[i][1])
            if x != y:
                parents[x] = y
                result -= 1
        return result

# BFS solution
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque
        ancestor, neighbor, nodes, result = 0, 1, {i: [-1, []] for i in range(n)}, n
        for edge in edges:
            nodes[edge[0]][neighbor].append(edge[1])
            nodes[edge[1]][neighbor].append(edge[0])
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            q = deque([i])
            visited[i] = True
            while q:
                u = q.popleft()
                for node in nodes[u][neighbor]:
                    if node != nodes[u][ancestor]:
                        if visited[node]:
                            continue
                        else:
                            visited[node] = True
                            q.append(node)
                            nodes[node][ancestor] = u
                            result -= 1
        return result

# DFS solution
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ancestor, neighbor, nodes, self.result = 0, 1, {i: [-1, []] for i in range(n)}, n
        for edge in edges:
            nodes[edge[0]][neighbor].append(edge[1])
            nodes[edge[1]][neighbor].append(edge[0])
        visited = [False] * n

        def dfs(u):
            visited[u] = True
            for node in nodes[u][neighbor]:
                if visited[node] and nodes[u][ancestor] != node:
                    continue
                if visited[node] is False:
                    nodes[node][ancestor] = u
                    self.result -= 1
                    dfs(node)
        for i in range(n):
            if not visited[i]:
                dfs(i)
        return self.result
