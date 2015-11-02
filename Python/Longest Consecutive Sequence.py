"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
"""

class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        if not num or len(num) == 0:
            return 0
        result, table = 1, {key : 0 for key in num}
        for number in num:
            if number not in table:
                continue
            lower, upper = number, number
            while upper + 1 in table:
                upper += 1
                del table[upper]
            while lower - 1 in table:
                lower -= 1
                del table[lower]
            if lower != upper:
                del table[number]
            result = max(result, upper - lower + 1)
        return result
