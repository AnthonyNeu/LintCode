"""
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Example
Given [1,2,3,4], k = 2, target = 5.

There are 2 solutions: [1,4] and [2,3].

Return 2.
"""

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        length = len(A)
        """
        dp[i][j][k] the number of j numbers in A[:i] which sums up to k
        """
        dp = [[[0 for _ in range(target + 1)] for _ in range(k + 1)] for _ in range(length + 1)]
        for i in range(length + 1):
            dp[i][0][0] = 1
        for i in range(1, length + 1):
            for j in range(1, min(k, i) + 1):
                for n in range(1, target + 1):
                    if A[i - 1] <= n:
                        dp[i][j][n] += dp[i - 1][j - 1][n - A[i - 1]]
                    dp[i][j][n] += dp[i - 1][j][n]
        return dp[-1][-1][-1]

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        length = len(A)
        dp = [[0 for _ in range(target + 1)] for _ in range(k + 1)]

        for i in range(1, length + 1):
            for j in reversed(range(1, min(k, i) + 1)):
                for n in reversed(range(A[i - 1], target + 1)):
                    if j == 1:
                        dp[j][n] += 1 if n == A[i - 1] else 0
                    else:
                        dp[j][n] += dp[j - 1][n - A[i - 1]]
        return dp[-1][-1]
