"""
Write an algorithm which computes the number of trailing zeros in n factorial.
"""

class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        result = 0
        while n > 0:
            result += n / 5
            n /= 5
        return result
