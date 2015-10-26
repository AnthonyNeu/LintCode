"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if not A or len(A) == 0:
            return True
        max_dist = 0
        for i in range(len(A)):
            if max_dist < i:
                return False
            max_dist = max(max_dist, i + A[i])
            if max_dist >= len(A) - 1:
                return True
