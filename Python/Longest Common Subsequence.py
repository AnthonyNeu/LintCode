"""
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.
"""

class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i, B_char in list(enumerate(B)):
            for j, A_char in list(enumerate(A)):
                if B_char == A_char:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
