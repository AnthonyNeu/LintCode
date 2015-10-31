"""
Given an array of integers, find a contiguous subarray which has the largest sum.
"""

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0
        max_value, max_end_here = nums[0], nums[0]
        for num in nums[1:]:
            max_end_here = max(max_end_here + num, num)
            max_value = max(max_end_here, max_value)
        return max_value
        