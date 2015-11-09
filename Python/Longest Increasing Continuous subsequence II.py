"""
Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. 
(The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).

Example
Given a matrix:

[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25

Challenge
O(nm) time and memory.
"""

class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        # Write your code here        
        if not A or len(A) == 0 or len(A[0]) == 0:
            return 0
        m, n = len(A), len(A[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        max_length = 0
        
        def dfs(x, y):
            if visited[x][y]:
                return dp[x][y]
            result = 1
            visited[x][y] = True
            for i in range(4):
                nx, ny = x + directions[i][0], y + directions[i][1]
                if 0 <= nx < m and 0 <= ny < n:
                    if A[nx][ny] > A[x][y]:
                        result = max(result, dfs(nx, ny) + 1)
            dp[x][y] = result
            return dp[x][y]
        for i in range(m):
            for j in range(n):
                dp[i][j] = dfs(i, j)
                max_length = max(dp[i][j], max_length)
        return max_length
