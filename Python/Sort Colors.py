"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        left, right, idx = 0, len(nums) - 1, 0
        while idx <= right:
            if nums[idx] == 0:
                nums[idx], nums[left] = nums[left], nums[idx]
                left += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[right] = nums[right], nums[idx]
                right -= 1
            else:
                idx += 1
