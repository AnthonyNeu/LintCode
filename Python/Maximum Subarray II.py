"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.
"""
# my solution, change from Maximum Subarray Difference
class Solution1:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here    
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        length = len(nums)
        max_ending_here = [nums[0]]
        for i in range(1, length):
            max_ending_here.append(max(max_ending_here[-1] + nums[i], nums[i]))
        max_starting_here = [nums[-1]]
        for i in reversed(range(length - 1)):
            max_starting_here = [max(max_starting_here[0] + nums[i], nums[i])] + max_starting_here
        max_subarray = [nums[-1]]
        # this is the max sum in the subarray[i:]
        for i in reversed(range(length - 1)):
            max_subarray = [max(max_subarray[0], max_starting_here[i])] + max_subarray
        max_sum = max([a + b for a, b in zip(max_ending_here[:length - 1], max_subarray[1:length])])
        return max_sum

class Solution2:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here    
        length = len(nums) 
        max_lr, max_rl = [float('-inf') for _ in range(length)], [float('-inf') for _ in range(length)]
        
        # compute max subarray from left to right
        max_lr_sum, cur_lr_sum = float('-inf'), 0
        for i in range(length):
            cur_lr_sum += nums[i]
            max_lr_sum = max(max_lr_sum, cur_lr_sum)
            max_lr[i] = max_lr_sum
            cur_lr_sum = max(0, cur_lr_sum)
        # compute max subarray from right to left
        max_rl_sum, cur_rl_sum = float('-inf'), 0
        for i in reversed(range(length)):
            cur_rl_sum += nums[i]
            max_rl_sum = max(max_rl_sum, cur_rl_sum)
            max_rl[i] = max_rl_sum
            cur_rl_sum = max(0, cur_rl_sum)
        return max([a + b for a, b in zip(max_lr[:length - 1], max_rl[1:length])])
