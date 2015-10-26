"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        if not A or len(A) == 0:
            return 0
        result, last, cur = 0, 0, 0
        for i in range(len(A)):
            if i > last:
                # if we still not reach the last one, return False
                if cur == last and last < len(A) - 1:
                    return float('inf')
                last = cur
                result += 1
            cur = max(cur, i + A[i])
        return result
