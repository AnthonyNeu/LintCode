"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        ways[i][j] = 1
                    elif i == 0:
                        ways[i][j] = ways[i][j - 1]
                    elif j == 0:
                        ways[i][j] = ways[i - 1][j]
                    else:
                        ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[m - 1][n - 1]
