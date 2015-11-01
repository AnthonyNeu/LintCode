"""
Given 3*n + 1 numbers, every numbers occurs triple times except one, find it.
"""

class Solution:
    """
	@param A : An integer array
	@return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        one, two, three = 0, 0, 0
        for num in A:
            # find digits count to 2 times
            two |= one & num
            # find digits count to 1 times
            one ^= num
            three = one & two
            one &= ~three
            two &= ~three
        return one
