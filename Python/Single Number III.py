"""
Given 2*n + 2 numbers, every numbers occurs twice except two, find them.
"""

class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        # write your code here
        x_xor_y = reduce(lambda x, y: x ^ y, A)

        bit = x_xor_y & -x_xor_y

        x = 0
        for i in A:
            if i & bit:
                x ^= i

        return [x, x ^ x_xor_y]
