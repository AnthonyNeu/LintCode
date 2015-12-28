"""
Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.

Example
Given N = 3 and the array [0, 1, 3], return 2.

Challenge
Do it in-place with O(1) extra memory and O(n) time.
"""

class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        result = len(nums)
        for i in range(len(nums)):
            result ^= nums[i]
            result ^= i
        return result

# swapping numbers to the same index cell
# https://leetcode.com/discuss/54454/swapping-numbers-to-the-same-index-cell
class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        cur, prev, n = 0, -1, len(nums)
        while cur < n:
            if nums[cur] != cur:
                if nums[cur] != n:
                    nums[cur], nums[nums[cur]] = nums[nums[cur]], nums[cur]
                else:
                    prev = cur
                    cur += 1
            else:
                cur += 1
        return n if prev == -1 else prev
