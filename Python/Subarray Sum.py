"""
Given an integer array, find a subarray where the sum of numbers is zero. 
Your code should return the index of the first number and the index of the last number.
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        result, table, cur = [], {}, 0
        for i, num in enumerate(nums):
            cur += num
            if cur == 0:
                return [0, i]
            if cur not in table:
                table[cur] = i
            else:
                return [table[cur] + 1, i]
