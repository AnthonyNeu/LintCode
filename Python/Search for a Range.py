"""
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].
"""

class Solution1:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here

        def searchStart():
            if A is None or len(A) == 0:
                return -1
            left, right = 0, len(A) - 1
            while left < right:
                mid = left + (right - left) / 2
                if A[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if A[left] == target else -1

        def searchEnd():
            if A is None or len(A) == 0:
                return -1
            left, right = 0, len(A) - 1
            while left < right:
                mid = left + (right - left) / 2
                if A[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            if target < A[left]:
                return left - 1 if left >= 1 else -1
            elif target > A[left]:
                return -1
            else:
                return left
        return [searchStart(), searchEnd()]

class Solution2:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return [-1, -1]
            
        def findPreviousIndex(left, right):
            if left > right:
                return right
            mid = left + (right - left) / 2
            if A[mid] >= target:
                return findPreviousIndex(left, mid - 1)
            else:
                return findPreviousIndex(mid + 1, right)

        def findNextIndex(left, right):
            if left > right:
                return left
            mid = left + (right - left) / 2
            if A[mid] <= target:
                return findNextIndex(mid + 1, right)
            else:
                return findNextIndex(left, mid - 1)
        previous_idx = findPreviousIndex(0, len(A) - 1)
        next_idx = findNextIndex(0, len(A) - 1)
        if previous_idx + 1 == next_idx:
            return [-1, -1]
        else:
            return [previous_idx + 1, next_idx - 1]
