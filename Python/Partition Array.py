"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.
"""

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        left, right, idx = 0, len(nums) - 1, 0
        while idx <= right:
            if nums[idx] < k:
                nums[left], nums[idx] = nums[idx], nums[left]
                idx += 1
                left += 1
            elif nums[idx] >= k:
                nums[right], nums[idx] = nums[idx], nums[right]
                right -= 1
        # for all elements larger than k
        if idx == 0:
            return 0
        # for all elements smaller than k
        elif idx == len(nums):
            return idx
        else:
            return left
