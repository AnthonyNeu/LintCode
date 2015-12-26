"""
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

Challenge
Rotate in-place with O(1) extra memory.
"""

class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if not s:
            return
        offset %= len(s)
        if offset == 0:
            return
        s.reverse()
        s[offset:] = s[:offset - 1:-1]
        s[:offset] = s[offset - 1::-1]

class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if not s:
            return
        offset %= len(s)
        def reverse(start, end):
            i, j = start, end
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        reverse(0, len(s) - offset - 1)
        reverse(len(s) - offset, len(s) - 1)
        reverse(0, len(s) - 1)
