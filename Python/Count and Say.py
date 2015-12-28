"""
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Example
Given n = 5, return "111221".

Note
The sequence of integers will be represented as a string.
"""

class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        s = '1'

        def get_next(s):
            result, idx = '', 0
            while idx < len(s):
                count = 1
                while idx < len(s) - 1 and s[idx] == s[idx + 1]:
                    count += 1
                    idx += 1
                result+= str(count) + s[idx]
                idx += 1
            return result
        while n > 1:
            s = get_next(s)
            n -= 1
        return s
