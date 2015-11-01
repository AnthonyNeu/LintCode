"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left, right = 1, x
        while left + 1 < right:
            mid = left + (right - left) / 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid
        if right * right <= x:
            return right
        return left
