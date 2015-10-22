"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return 0
        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if target <= A[-1] else left + 1
        