"""
Write an algorithm to determine if a number is happy.

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example
19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        s = set([n])
        while True:
            num = 0
            while n != 0:
                num += (n % 10) ** 2
                n /= 10
            if num == 1:
                return True
            if num in s:
                return False
            n = num
            s.add(num)

# use slow, fast pointer to find the cycle
class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here

        def digit_square_sum(n):
            result = 0
            while n:
                tmp = n % 10
                result += tmp * tmp
                n /= 10
            return result
        slow, fast = n, n
        while True:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(fast)
            fast = digit_square_sum(fast)
            if slow == 1:
                return True
            if slow == fast:
                return False
