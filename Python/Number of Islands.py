"""
Given a boolean 2D matrix, find the number of islands.
"""

class Solution1:
    def __init__(self):
        self.dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid: return 0
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        cnt = 0
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and grid[i][j]:
                    cnt += 1
                    self.dfs(grid, i, j, visited)

        return cnt

    def dfs(self, grid, i, j, visited):
        # pre-call check
        m = len(grid)
        n = len(grid[0])
        visited[i][j] = True
        for dir in self.dirs:
            i1 = i+dir[0]
            j1 = j+dir[1]
            if 0 <= i1 < m and 0 <= j1 < n and not visited[i1][j1] and grid[i1][j1]:
                self.dfs(grid, i1, j1, visited)

class Solution2:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if len(grid) == 0:
            return 0
        M = len(grid)
        N = len(grid[0])
        
        island = [[False for _ in xrange(N)] for _ in xrange(M)]
        def markIsland(island,i,j):
            if i < M-1:
                if grid[i+1][j] and island[i+1][j] is False:
                    island[i+1][j] = True
                    markIsland(island,i+1,j)
            if j < N-1:
                if grid[i][j+1] and island[i][j+1] is False:
                    island[i][j+1] = True
                    markIsland(island,i,j+1)
            if i >= 1:
                if grid[i-1][j] and island[i-1][j] is False:
                    island[i-1][j] = True
                    markIsland(island,i-1,j)
            if j >= 1:
                if grid[i][j-1] and island[i][j-1] is False:
                    island[i][j-1] = True
                    markIsland(island,i,j-1)
        count = 0
        for i in xrange(M):
            for j in xrange(N):
                if island[i][j] is False and grid[i][j]:
                    count +=1
                    island[i][j] = True
                    markIsland(island,i,j)
                    
        return count