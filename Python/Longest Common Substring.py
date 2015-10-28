"""
Given two strings, find the longest common substring.

Return the length of it.
"""

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i, B_char in list(enumerate(B)):
            for j, A_char in list(enumerate(A)):
                if A_char == B_char:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return max([max(dp[i][:]) for i in range(n + 1)])
