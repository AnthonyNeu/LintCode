"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return False
        
        def searchHelper(left, right):
            while left <= right:
                mid = left + (right - left) / 2
                if A[mid] == target:
                    return True
                if A[left] < A[mid]:
                    if A[mid] > target and A[left] <= target:
                        right = mid
                    else:
                        left = mid + 1
                elif A[left] > A[mid]:
                    if A[mid] < target and A[left] >= target:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    left += 1
            return False
        return searchHelper(0, len(A) - 1)
