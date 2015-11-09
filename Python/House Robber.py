"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example
Given [3, 8, 4], return 8.

Challenge
O(n) time and O(1) memory.
"""

class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if not A or len(A) == 0:
            return 0
        dp = [0 for _ in range(len(A) + 1)]
        dp[1] = A[0]
        for i in range(2, len(A) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
        return dp[-1]

class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if not A or len(A) == 0:
            return 0
        prev, cur = 0, A[0]
        for i in range(2, len(A) + 1):
            prev, cur = cur, max(prev + A[i - 1], cur)
        return cur
