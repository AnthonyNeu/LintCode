"""
Given a big sorted array, find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.
"""

class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        left, right = 0, 1
        while right < len(A) and A[right] <= target:
            right *= 10

        def binarySearch(nums, target):
            if nums is None or len(nums) == 0:
                return -1
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) / 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if nums[left] == target else -1
        return binarySearch(A[:right], target)
