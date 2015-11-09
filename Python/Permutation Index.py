"""
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

http://www.geekviewpoint.com/python/numbers/permutation_index

Example
Given [1,2,4], return 1.
"""

class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        # Write your code here
        index = 0
        position = 2 # position 1 is paired with factor 0 and so is skipped
        factor = 1
        for p in range( len( A ) - 2, -1, -1 ):
            successors = 0
            for q in range( p + 1, len( A ) ):
                if A[p] > A[q]:
                    successors += 1
            index += ( successors * factor )
            factor *= position
            position += 1
        return index + 1
