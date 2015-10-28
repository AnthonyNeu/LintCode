"""
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?
"""

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        for i in range(len(A)):
            for j in reversed(range(m + 1)):
                dp[j] = dp[j]
                if j >= A[i] and dp[j - A[i]]:
                    dp[j] = True
        for i in reversed(range(m + 1)):
            if dp[i]:
                return i
        return 0
