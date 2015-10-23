"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        
        def searchHelper(left, right):
            while left <= right:
                mid = left + (right - left) / 2
                if A[mid] == target:
                    return mid
                if A[left] <= A[mid]:
                    if A[mid] > target and A[left] <= target:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    if A[mid] < target and A[left] >= target:
                        left = mid + 1
                    else:
                        right = mid
            return -1
        return searchHelper(0, len(A) - 1)
        