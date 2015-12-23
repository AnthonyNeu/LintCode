"""
Calculate the a^n % b where a, b and n are all 32bit integers.

Example
For 231 % 3 = 2

For 1001000 % 1000 = 0

Challenge
O(logn)
"""

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b
        if n % 2 == 0:
            cache = self.fastPower(a, b, n / 2)
            return (cache * cache) % b
        else:
            cache = self.fastPower(a, b, n / 2)
            return (a * cache * cache) % b
