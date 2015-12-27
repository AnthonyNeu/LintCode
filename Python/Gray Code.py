"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, find the sequence of gray code. 
A gray code sequence must begin with 0 and with cover all 2^n integers.

Example
Given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note
For a given n, a gray code sequence is not uniquely defined.

[0,2,3,1] is also a valid gray code sequence according to the above definition.
"""

class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        # Write your code here
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        result = self.grayCode(n - 1)
        length, x = len(result), 1 << (n - 1)
        for i in reversed(range(length)):
            result.append(result[i] + x)
        return result

# https://leetcode.com/discuss/13058/share-my-simple-way-of-this-problem-_
class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        # Write your code here
        result = []
        for i in range(1 << n):
            result.append(i >> 1 ^ i)
        return result
