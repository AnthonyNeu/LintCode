"""
Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater than a given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|
"""

class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return 0
        m = len(A)
        dp = [[float('inf') for _ in range(101)] for _ in range(m)]
        for i in range(m):
            for j in range(1, 101):
                if i == 0:
                    dp[i][j] = abs(j - A[i])
                else:
                    for k in range(1, 101):
                        if abs(k - j) > target:
                            continue
                        else:
                            dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(A[i] - j))
        return min(dp[m - 1][:])
