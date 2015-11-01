"""
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
"""

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        result = 0
        for num in A:
            result ^= num
        return result
