"""
Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

Example
Given the permutation [1, 4, 2, 2], return 3.
"""

class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndexII(self, A):
        # Write your code here
        from collections import defaultdict
        # position 1 is paired with factor 0 and so is skipped
        index, position, factor, counter = 0, 2, 1, defaultdict(int)
        counter[A[-1]] += 1
        for p in range( len( A ) - 2, -1, -1 ):
            successors = defaultdict(int)
            counter[A[p]] += 1
            for q in range( p + 1, len( A ) ):
                if A[p] > A[q]:
                    successors[A[q]] += 1
            for value in successors.values():
                index += (factor * value / counter[A[p]])
            factor = factor * position / counter[A[p]]
            position += 1
        return index + 1
