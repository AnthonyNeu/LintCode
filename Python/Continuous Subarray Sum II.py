"""
Given an integer array, find a continuous rotate subarray where the sum of numbers is the biggest. 
Your code should return the index of the first number and the index of the last number. 
(If their are duplicate answer, return anyone. The answer can be rorate array or non- rorate array)

Example
Give [3, 1, -100, -3, 4], return [4,1].
"""


class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):
        # Write your code here
        if not A or len(A) == 0:
            return 0
        max_value, max_ending_here = A[0], A[0]
        max_start, max_ending_start, max_ending_end = 0, 0, 0
        total = A[0]
        result = [0, 0]
        for i in range(1, len(A)):
            total += A[i]
            if max_ending_here < 0:
                max_ending_start = max_ending_end = i
                max_ending_here = A[i]
            else:
                max_ending_here += A[i]
                max_ending_end = i
            if max_value <= max_ending_here:
                # update the result
                result = [max_ending_start, max_ending_end]
                max_value = max_ending_here
        min_ending_here, min_ending_start, min_ending_end = 0, 0, -1
        # calculate the min sum from the start
        for i in range(len(A)):
            if min_ending_here > 0:
                min_ending_here = A[i]
                min_ending_start, min_ending_end = i, i
            else:
                min_ending_here += A[i]
                min_ending_end = i
            if min_ending_start == 0 and min_ending_end == len(A) - 1:
                continue
            if total - min_ending_here >= max_value:
                max_value = total - min_ending_here
                result = [(min_ending_end + 1) % len(A), (min_ending_start - 1 + len(A)) % len(A)]
        return result
