"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.

Example
Given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.
"""

class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        if not nums or len(nums) == 0:
            return -1
        start, end, cur_sum = 0, 0, 0
        while end < len(nums):
            cur_sum += nums[end]
            if cur_sum < s:
                end += 1
            else:
                break
        if cur_sum < s:
            return -1
        min_length = end - start + 1
        end += 1
        while end < len(nums):
            cur_sum += nums[end]
            while start <= end:
                if cur_sum - nums[start] >= s:
                    cur_sum -= nums[start]
                    start += 1
                else:
                    break
            min_length = min(min_length, end - start + 1)
            end += 1
        return min_length
