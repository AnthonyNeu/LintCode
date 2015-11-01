"""
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.
"""

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        length = len(nums)
        # dp[i][j] the max of j non-overlapping subarry in nums[:i]
        dp = [[float('-inf') for _ in range(k + 1)] for _ in range(length + 1)]
        dp[0][0] = 0
        for i in range(length + 1):
            dp[i][0] = 0
        for i in range(1, length + 1):
            for j in range(1, min(i, k) + 1):
                dp[i][j] = dp[i - 1][j]
                # find the dp[i][j] by end at any index between i and j
                # this is the same as find the max subarray start at index p
                max_sum_start_at_p = float('-inf')
                for p in reversed(range(j, i + 1)):
                    max_sum_start_at_p = max(nums[p - 1], max_sum_start_at_p + nums[p - 1])
                    dp[i][j] = max(dp[i][j], dp[p - 1][j - 1] + max_sum_start_at_p)
        return dp[-1][-1]
