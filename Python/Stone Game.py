"""
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.

The score is the number of stones in the new pile.

You are to determine the minimum of the total score.

Example
[3, 4, 3] return 17

[1, 1, 1, 1] return 8

[4, 4, 5, 9] return 43

http://www.bubuko.com/infodetail-439987.html
"""

class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        # Write your code here
        if not A:
            return 0
        length = len(A)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]
        sum_cache = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            sum_cache[i][i] = A[i]
            for j in range(i + 1, length):
                sum_cache[i][j] = sum_cache[i][j - 1] + A[j]
        for l in range(2, length + 1):
            for i in range(1, length + 2 - l):
                j = i + l - 1
                dp[i][j] = float('inf')
                for p in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][p] + dp[p + 1][j] + sum_cache[i - 1][j - 1])
        return dp[1][length]
