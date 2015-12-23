"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Example
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        start, end = 0, 1
        while end < len(A):
            if A[end] != A[start]:
                if end - start > 1:
                    A[start + 1] = A[end]
                    start += 1
                else:
                    start = end
            end += 1
        return start + 1
