"""
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
"""

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        left, right = 0, len(A) - 1
        while left <= right:
            if A[left] == elem:
                A[left], A[right] = A[right], A[left]
                right -= 1
            else:
                left += 1
        return left
