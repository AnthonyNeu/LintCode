"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O''s into 'X''s in that surrounded region.

Example
X X X X
X O O X
X X O X
X O X X
After capture all regions surrounded by 'X', the board should be:

X X X X
X X X X
X X X X
X O X X
"""


# BFS
from collections import deque
class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        if not board:
            return
        current, m, n = deque([]), len(board), len(board[0])
        # only need to do bfs from the outer layer
        for i in range(m):
            current.append((i, 0))
            current.append((i, n - 1))
        for i in range(n):
            current.append((0, i))
            current.append((m - 1, i))
        while current:
            x, y = current.popleft()
            if board[x][y] in ('O', 'V'):
                board[x][y] = 'V'
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                        board[i][j] = 'V'
                        current.append((i, j))
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

# DFS
class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'V'
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
        for i in range(m):
            dfs(i, 0)
            if n > 1:
                dfs(i, n - 1)
        for i in range(n):
            dfs(0, i)
            if m > 1:
                dfs(m - 1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

# Union find by weight quick union with path compression
# http://algs4.cs.princeton.edu/15uf/
class union_find:
    def __init__(self, size):
        self.father = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]

    def find(self, x):
        parent = self.father[x]
        while parent != self.father[parent]:
            parent = self.father[parent]
        return parent

    def compressed_find(self, x):
        parent = self.father[x]
        while parent != self.father[parent]:
            parent = self.father[parent]
        # set all father to be parent we just get
        prev_father = self.father[x]
        while prev_father != self.father[prev_father]:
            prev_father, self.father[prev_father] = self.father[prev_father], parent
        return parent

    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.father[i] = j
        elif self.rank[i] > self.rank[j]:
            self.father[j] = i
        else:
            self.father[j] = i
            self.rank[i] += 1

class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        uf = union_find(m * n + 1)
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                    uf.union(i * n + j, m * n)
                elif board[i][j] == 'O':
                    if board[i - 1][j] == 'O':
                        uf.union(i * n + j, (i - 1) * n + j)
                    if board[i + 1][j] == 'O':
                        uf.union(i * n + j, (i + 1) * n + j)
                    if board[i][j - 1] == 'O':
                        uf.union(i * n + j, i * n + j - 1)
                    if board[i][j + 1] == 'O':
                        uf.union(i * n + j, i * n + j + 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and uf.compressed_find(i * n + j) != uf.compressed_find(m * n):
                    board[i][j] = 'X'
