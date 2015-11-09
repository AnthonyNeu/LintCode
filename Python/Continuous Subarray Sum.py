"""
Given an integer array, find a continuous subarray where the sum of numbers is the biggest. 
Your code should return the index of the first number and the index of the last number. 
(If their are duplicate answer, return anyone)

Example
Give [-3, 1, 3, -3, 4], return [1,4].
"""

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        if not A or len(A) == 0:
            return 0
        max_value, max_ending_here = A[0], A[0]
        max_start, max_end_start = 0, 0
        result = [0, 0]
        for i in range(1, len(A)):
            if A[i] > max_ending_here + A[i]:
                max_end_start = i
                max_ending_here = A[i]
            else:
                max_ending_here += A[i]
            if max_value < max_ending_here:
                # update the result
                result = [max_end_start, i]
                max_value = max_ending_here
        return result
