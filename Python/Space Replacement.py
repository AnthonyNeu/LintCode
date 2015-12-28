"""
Write a method to replace all spaces in a string with %20. The string is given in a characters array, you can assume it has enough space for replacement and you are given the true length of the string.

You code should also return the new length of the string after replacement.

Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith".

Note
If you are using Java or Python，please use characters array instead of string.

Challenge
Do it in-place.
"""

# two passes solution
class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if not string:
            return 0
        count = 0
        for i in range(length):
            if string[i] == ' ':
                count += 1
        new_length = length + 2 * count
        string += [''] * 2 * count
        j = 1
        for i in reversed(range(length)):
            if string[i] != ' ':
                string[new_length - j] = string[i]
                j += 1
            else:
                string[new_length - j ] = '0'
                j += 1
                string[new_length - j ] = '2'
                j += 1
                string[new_length - j ] = '%'
                j += 1
        return new_length
