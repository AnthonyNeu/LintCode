"""
Given a string, find all permutations of it without duplicates.

Example
Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].
"""

from collections import Counter
class Solution:
    # @param {string} str a string
    # @return {string[]} all permutations
    def stringPermutation2(self, str):
        # Write your code here
        counter = Counter(str)
        result = []
        def dfs(current):
            if len(current) == len(str):
                result.append(current)
            for c in counter:
                if counter[c] > 0:
                    counter[c] -= 1
                    if counter[c] == 0:
                        del counter[c]
                    dfs(current + c)
                    if c not in counter:
                        counter[c] = 0
                    counter[c] += 1
        dfs("")
        return result
