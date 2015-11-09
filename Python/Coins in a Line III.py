"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.

Challenge
Follow Up Question:

If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n) time?
"""

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        if n % 2 == 0 and self.firstWillWinEven(values):
            return True
        length = len(values)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]
        visited = [[False for _ in range(length + 1)] for _ in range(length + 1)]
        """
        dp[x][y] is the max value of coin the first player can get if there are
        still pos x to pos y's coins left, so
        Case 1: player 1 takes the left, player 2 takes left or right
        Case 2: player 1 takes the right, player 2 takes left or right
        dp[x][y] = max(min(dp[x+2][y], dp[x+1][y-1])+ values[x]) , (min(dp[x][y
        -2], dp[x+1][y-1])+ values[y])
        """
        def dfs(start, end):
            if visited[start][end]:
                return dp[start][end]
            visited[start][end] = True
            if start > end:
                dp[start][end] = 0
            elif start + 1 >= end:
                dp[start][end] = max(values[start], values[end])
            else:
                pick_start = min(dfs(start + 2, end), dfs(start + 1, end - 1)) + values[start]
                pick_end = min(dfs(start, end - 2), dfs(start + 1, end - 1)) + values[end]
                dp[start][end] = max(pick_start, pick_end)
            return dp[start][end]
        return sum(values) < 2 * dfs(0, length - 1)

    def firstWillWinEven(self, values):
        """
        odd_s: sum of values at odd position
        even_s: sum of values at even position
        if odd_s == even_s, the first mover cannot win if the other player mimics the first player
        if odd_s > even_s, the first mover chooses the odd position values, and FORCE the other player choose the even
        position values. The strategy and outcome are similar when even_s > odd_s.
          
        :param values:
        :return:
        """
        odd_s = 0
        even_s = 0
        for i in xrange(len(values)):
            if i % 2 == 0:
                even_s += values[i]
            else:
                odd_s += values[i]

        return odd_s != even_s
