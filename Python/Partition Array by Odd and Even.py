"""
Partition an integers array into odd number first and even number second.

Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge
Do it in-place.
"""

class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        index, left, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] % 2 == 1:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            else:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
