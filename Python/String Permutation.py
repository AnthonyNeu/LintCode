"""
Given two strings, write a method to decide if one is a permutation of the other.

Example
abcd is a permutation of bcad, but abbe is not a permutation of abe
"""

class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        from collections import Counter
        counter1 = Counter(A)
        counter2 = Counter(B)
        return all([counter1[key] == counter2[key] for key in counter1]) and all([counter1[key] == counter2[key] for key in counter2])
