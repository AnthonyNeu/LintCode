"""
Using O(1) time to check whether an integer n is a power of 2.
"""

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n == 0:
            return False
        return n & (n - 1) == 0
