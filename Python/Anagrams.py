"""
Given an array of strings, return all groups of strings that are anagrams.

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Note
All inputs will be in lower-case
"""

from collections import defaultdict
class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        lookup = defaultdict(list)
        for string in strs:
            lookup[''.join(sorted(string))].append(string)
        result = []
        for string in lookup:
            if len(lookup[string]) > 1:
                result.extend(lookup[string])
        return result
