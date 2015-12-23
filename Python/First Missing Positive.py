"""
Given an unsorted integer array, find the first missing positive integer.

Example
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Challenge
Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        i, n = 0, len(A)
        while i < n:
            if A[i] > 0 and A[i] <= n and A[i] != A[A[i] - 1]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            else:
                 i += 1
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1
