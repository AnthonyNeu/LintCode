"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        if m == 0 or n == 0:
            return 0
        ways = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways[i][j] = 1
                elif i == 0:
                    ways[i][j] = ways[i][j - 1]
                elif j == 0:
                    ways[i][j] = ways[i - 1][j]
                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[m - 1][n - 1]
