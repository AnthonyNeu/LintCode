"""
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first play will win or lose?

Example
n = 1, return true.

n = 2, return true.

n = 3, return false.

n = 4, return true.

n = 5, return true.

Challenge
O(n) time and O(1) memory
"""

class Solution1:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        return not (n % 3 == 0)

# DP solution
class Solution2:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        dp = [False for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        
        def dfs(n):
            if visited[n]:
                return dp[n]
            visited[n] = True
            if n <= 0:
                dp[n] = False
            elif n == 1 or n == 2:
                dp[n] = True
            elif n == 3:
                dp[n] = False
            else:
                if (dfs(n - 2) and dfs(n - 3)) or (dfs(n - 3) and dfs(n - 4)):
                    dp[n] = True
                else:
                    dp[n] = False
            return dp[n]
        return dfs(n)
