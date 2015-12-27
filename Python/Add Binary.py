"""
Given two binary strings, return their sum (also a binary string).

Example
a = 11

b = 1

Return 100
"""

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        result = ''
        length, carry = max(len(a), len(b)), 0
        for i in range(length):
            ai = 0 if i >= len(a) else ord(a[len(a) - i - 1]) - ord('0')
            bi = 0 if i >= len(b) else ord(b[len(b) - i - 1]) - ord('0')
            val = ai + bi + carry
            carry = val / 2
            result = str(val % 2) + result
        if carry > 0:
            result = str(carry) + result
        return result
