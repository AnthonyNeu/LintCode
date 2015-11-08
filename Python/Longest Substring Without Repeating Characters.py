"""
Given a string, find the length of the longest substring without repeating characters.

Example
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        start, end, look_up = 0, 0, {}
        while end < len(s):
            if s[end] not in look_up:
                look_up[s[end]] = end
                end += 1
            else:
                break
        max_length = end - start
        while end < len(s):
            if s[end] not in look_up:
                look_up[s[end]] = end
                max_length = max(max_length, end - start + 1)
            else:
                index = look_up[s[end]]
                while start <= index:
                    del look_up[s[start]]
                    start += 1
                look_up[s[end]] = end
            end += 1
        return max_length
