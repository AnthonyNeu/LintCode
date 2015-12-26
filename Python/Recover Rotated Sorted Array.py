"""
Given a rotated sorted array, recover it to sorted array in-place.

Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge
In-place, O(1) extra space and O(n) time.

Clarification
What is rotated array?

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
"""

class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        p = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                p = i

        def reverse(start, end):
            i, j = start, end
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if p != -1:
            reverse(0, len(nums) - 1)
            reverse(0, len(nums) - p - 2)
            reverse(len(nums) - p - 1, len(nums) - 1)
