"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        left, right = 0, len(num) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if num[mid] > num[right]:
                left = mid
            elif num[mid] < num[right]:
                right = mid
            else:
                right -= 1
        return min(num[left], num[right])
        