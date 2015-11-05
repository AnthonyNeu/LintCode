"""
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.
"""

class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        if not nums or len(nums) == 0:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1
            while left + 1 < right:
                mid = left + (right - left) / 2
                if nums[mid] + nums[i] > target:
                    right = mid
                else:
                    left = mid
            if nums[i] + nums[left] > target:
                count += len(nums) - left
            elif nums[i] + nums[right] > target:
                count += len(nums) - right
        return count
