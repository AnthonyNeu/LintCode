"""
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peek if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.
"""

class Solution1:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        left, right = 1, len(A) - 2
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < A[mid - 1]:
                right = mid
            elif A[mid] < A[mid + 1]:
                left = mid
            else:
                right = mid
        if A[left] < A[right]:
            return right
        else:
            return left

class Solution2:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        def findPeakHelper(left, right):
            if left == right:
                return left
            mid = left + (right - left) / 2
            if A[mid] > A[mid + 1]:
                return findPeakHelper(left, mid)
            else:
                return findPeakHelper(mid + 1, right)
        return findPeakHelper(1, len(A) - 2)
