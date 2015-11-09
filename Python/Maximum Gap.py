"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example
Given [1, 9, 2, 5], the sorted form of it is [1, 2, 5, 9], the maximum gap is between 5 and 9 = 4.

Note
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Challenge
Sort is easy but will cost O(nlogn) time. Try to solve it in linear time and space.
"""

class Solution:
     # @param nums: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        # write your code here
        if len(nums) < 2:
            return 0
        Max = -1
        Min = float('inf')
        for i in xrange(len(nums)):
            if nums[i] < Min:
                Min = nums[i]
            if nums[i] > Max:
                Max = nums[i]

        gap = (Max - Min)/len(nums) + 1
        minGap = [-1 for _ in range((Max - Min)/gap + 1)]
        maxGap = [-1 for _ in range((Max - Min)/gap + 1)]

        for i in xrange(len(nums)):
            if minGap[(nums[i]-Min)/gap] == -1:
                minGap[(nums[i]-Min)/gap] = nums[i]
                maxGap[(nums[i]-Min)/gap] = nums[i]
            else:
                if minGap[(nums[i]-Min)/gap] > nums[i]:
                    minGap[(nums[i]-Min)/gap] = nums[i]
                elif maxGap[(nums[i]-Min)/gap] < nums[i]:
                    maxGap[(nums[i]-Min)/gap] = nums[i]

        maxInterval = 0
        start = minGap[0]
        for i in xrange(len(minGap)):
            if minGap[i] != maxGap[i] or (minGap[i] == maxGap[i] and maxGap[i] != -1):
                end = minGap[i]
                maxInterval = max(maxInterval,end - start)
                start = maxGap[i]
        return max(maxInterval,end - start)
