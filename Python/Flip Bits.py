"""
Determine the number of bits required to flip if you want to convert integer n to integer m.

Example
Given n = 31 (11111), m = 14 (01110), return 2.

Note
Both n and m are 32-bit integers.
"""

class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        c = a ^ b
        result, count = 0, 0
        while c != 0 and count < 32:
            if c & 1 == 1:
                result += 1
            c >>= 1
            count += 1
        return result
