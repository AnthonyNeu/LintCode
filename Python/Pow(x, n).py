"""
Implement pow(x, n).

Note
You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

Challenge
O(logn) time
"""

class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        if n == 0:
            return 1
        if n == 1:
            return x
        negative = False if n > 0 else True
        n = abs(n)
        k = n / 2
        l = n - 2 * k
        t1, t2 = self.myPow(x, k), self.myPow(x, l)
        if negative:
            return 1 / float(t1 * t1 * t2)
        else:
            return t1 * t1 * t2

# iterative solutions
class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result
