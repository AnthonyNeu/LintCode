"""
Given an array with integers.

Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest.

Return the largest difference.
"""

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if not nums or len(nums) <= 1:
            return 0
        length = len(nums)
        max_ending_here, min_ending_here = [nums[0]], [nums[0]]
        for i in range(1, length):
            max_ending_here.append(max(max_ending_here[-1] + nums[i], nums[i]))
            min_ending_here.append(min(min_ending_here[-1] + nums[i], nums[i]))
        max_starting_here, min_starting_here = [nums[-1]], [nums[-1]]
        for i in reversed(range(length - 1)):
            max_starting_here = [max(max_starting_here[0] + nums[i], nums[i])] + max_starting_here
            min_starting_here = [min(min_starting_here[0] + nums[i], nums[i])] + min_starting_here
        # there are two situations
        # the max sum array in the previous
        # or in the latter
        max_difference = max([abs(a - b) for a, b in zip(max_ending_here[:length - 1], min_starting_here[1:length])])
        _max_difference = max([abs(a - b) for a, b in zip(min_ending_here[:length - 1], max_starting_here[1:length])])
        return max(max_difference, _max_difference)
