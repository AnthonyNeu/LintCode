"""
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.
"""

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0
        min_value, min_end_here = nums[0], nums[0]
        for num in nums[1:]:
            min_end_here = min(min_end_here + num, num)
            min_value = min(min_end_here, min_value)
        return min_value
