"""
Given a string s, find the length of the longest substring T that contains at most k distinct characters.

Example
For example, Given s = "eceba", k = 3,

T is "eceb" which its length is 4.
"""

class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        from collections import defaultdict
        if k == 0:
            return 0
        start, end, look_up, max_length = 0, 0, defaultdict(int), 0
        while end < len(s):
            while end < len(s) and (s[end] in look_up or len(look_up) < k):
                look_up[s[end]] += 1
                end += 1
            max_length = max(max_length, end - start)
            while start < end and len(look_up) == k:
                look_up[s[start]] -= 1
                if look_up[s[start]] == 0:
                    del look_up[s[start]]
                start += 1
        return max_length
