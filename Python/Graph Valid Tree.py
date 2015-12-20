"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

from collections import deque

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if len(edges) != n - 1:
            return False
        ancestor, neighbor, nodes = 0, 1, {i: [-1, []] for i in range(n)}
        for edge in edges:
            nodes[edge[0]][neighbor].append(edge[1])
            nodes[edge[1]][neighbor].append(edge[0])
        visited = [False] * n
        q = deque([0])
        visited[0] = True
        # BFS to find cycle
        while q:
            u = q.popleft()
            for node in nodes[u][neighbor]:
                if node != nodes[u][ancestor]:
                    if visited[node]:
                        return False
                    else:
                        visited[node] = True
                        q.append(node)
                        nodes[node][ancestor] = u
        return all(visited)


# use union find
class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        parents = [i for i in range(n)]

        def find(i):
            if parents[i] == i:
                return i
            else:
                return find(parents[i])
        for i in range(len(edges)):
            x, y = find(edges[i][0]), find(edges[i][1])
            if x == y:
                return False
            parents[x] = y
        return len(edges) == n - 1


# use DFS to find cycle
class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if len(edges) != n - 1:
            return False
        ancestor, neighbor, nodes = 0, 1, {i: [-1, []] for i in range(n)}
        for edge in edges:
            nodes[edge[0]][neighbor].append(edge[1])
            nodes[edge[1]][neighbor].append(edge[0])
        visited = [False] * n

        def has_cycle(u):
            visited[u] = True
            for node in nodes[u][neighbor]:
                if visited[node] and nodes[u][ancestor] != node:
                    return True
                if visited[node] is False:
                    nodes[node][ancestor] = u
                    if has_cycle(node):
                        return True
            return False
        if has_cycle(0):
            return False
        return all(visited)
