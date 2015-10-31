"""
Given a string which contains only letters. Sort it by lower case first and upper case second.
"""

class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] == chars[left].upper():
                chars[left], chars[right] = chars[right], chars[left]
                right -= 1
            else:
                left += 1
