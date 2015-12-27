"""
Reverse digits of an integer. Returns 0 when the reversed integer overflows (signed 32-bit integer).


Reverse digits of an integer. Returns 0 when the reversed integer overflows (signed 32-bit integer).

Have you met this question in a real interview? Yes
Example
Given x = 123, return 321

Given x = -123, return -321
"""

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        sign = -1 if n < 0 else 1
        count, result, n, int_max_prefix = 0, 0, abs(n), 214748364
        while n != 0:
            result = result * 10 + n % 10
            n /= 10
            count += 1
            if count == 9 and n > 0 and result % (10 ** 8) > 2:
                return 0
            if sign == 1 and result >= int_max_prefix and n > 7:
                return 0
            if sign == -1 and result >= int_max_prefix + 1 and n > 8:
                return 0
        return result * sign

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        sign = 1 if n > 0 else -1
        result, n = 0, abs(n)
        while n != 0:
            if result > 214748364:
                return 0
            result = result * 10 + n % 10
            n /= 10
        return result * sign
