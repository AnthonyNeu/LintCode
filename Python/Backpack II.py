"""
Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?
"""

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        dp = [0 for _ in range(m + 1)]
        for i in range(len(A)):
            for j in reversed(range(m + 1)):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j - A[i]] + V[i])
        return max(dp)
