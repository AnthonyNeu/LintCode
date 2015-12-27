"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Example
Given [1,2,3] which represents 123, return [1,2,4].

Given [9,9,9] which represents 999, return [1,0,0,0].
"""

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        result, carry = [], 1
        for i in reversed(range(len(digits))):
            val = carry + digits[i]
            result.append(val % 10)
            carry = val / 10
        if carry > 0:
            result.append(carry)
        return result[::-1]
