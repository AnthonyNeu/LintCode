"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
"""

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle or len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        m, n = len(triangle), len(triangle[0])
        dp = [float('inf') for _ in range(len(triangle[m - 1]))]
        dp[0] = triangle[0][0]
        for i in range(1, m):
            for j in reversed(range(len(triangle[i]))):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
        return min(dp)
        