"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return 2147483647

Example
Given dividend = 100 and divisor = 9, return 11.
"""

class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        """
        O(log n) times, O(1) space
        a = (2^n * an + ... + 2^1 * a1 + 2^0 * a0)
        We calculate the result of 2^n * an divide by divisor and sum up all the result.
        Similarly, we transfer the number into a new number based on divisor:
        a = (d^n * an + ... + d^1 * a1 + d^0 * a0)
        And then sum up all the an*d^n to get the result.
        """
        result = 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        dvd = abs(dividend)
        dvs = abs(divisor)
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        while dvd >= dvs:
            count, dd = 1, dvs
            while dvd >= dd:
                dvd -= dd
                result += count
                if dd < (2147483647 >> 1):
                    dd += dd
                    count += count
        return result * sign
