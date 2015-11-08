"""
Given a string source and a string target, find the minimum window in source which will contain all the characters in target.

Example
source = "ADOBECODEBANC" target = "ABC" Minimum window is "BANC".

Note
If there is no such window in source that covers all characters in target, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in source.

Challenge
Can you do it in time complexity O(n) ?

Clarification
Should the characters in minimum window has the same order in target?

    - Not necessary.
"""

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        current_count = [0 for i in xrange(256)]
        expected_count = [0 for i in xrange(256)]
        for char in target:
            expected_count[ord(char)] += 1
        i, count, start, min_width, min_start = 0, 0, 0, float("inf"), 0
        while i < len(source):
            index = ord(source[i])
            current_count[index] += 1
            if current_count[index] <= expected_count[index]:
                count += 1
            if count == len(target):
                index = ord(source[start])
                while expected_count[index] == 0 or \
                      current_count[index] > expected_count[index]:
                    current_count[index] -= 1
                    start += 1
                    index = ord(source[start])
                if min_width > i - start + 1:
                    min_width = i - start + 1
                    min_start = start
            i += 1
        if min_width == float("inf"):
            return ""
        return source[min_start:min_start + min_width]
