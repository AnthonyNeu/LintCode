"""
There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

Example
Given values array A = [1,2,2], return true.

Given A = [1,2,4], return false.
"""

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if not values or len(values) == 0:
            return False
        length = len(values)
        dp = [0 for _ in range(length + 1)]
        visited = [False for _ in range(length + 1)]
        
        def dfs(n):
            if visited[n]:
                return dp[n]
            visited[n] = True
            if n == 0:
                dp[0] = 0
            elif n == 1:
                dp[1] = values[length - 1]
            elif n == 2:
                dp[2] = values[length - 1] + values[length - 2]
            elif n == 3:
                dp[3] = values[length - 2] + values[length - 3]
            else:
                dp[n] = max(min(dfs(n - 2), dfs(n - 3)) + values[length - n], min(dfs(n - 3), dfs(n - 4)) + values[length - n] + values[length - n + 1])
            return dp[n]
        return sum(values) < 2 * dfs(length)
