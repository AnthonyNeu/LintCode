"""
Given a target number and an integer array sorted in ascending order. 
Find the total number of occurrences of target in the array.

Example
Given [1, 3, 3, 4, 5] and target = 3, return 2.

Given [2, 2, 3, 4, 6] and target = 4, return 1.

Given [1, 2, 3, 4, 5] and target = 6, return 0.

Challenge
Time complexity in O(logn)
"""

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        if not A:
            return 0
        length = len(A)
        def find_idx(comp, choose):
            left, right = 0, length - 1
            while left + 1 < right:
                mid = left + (right - left) / 2
                if comp(mid):
                    right = mid
                else: 
                    left = mid
            if A[left] != target and A[right] != target:
                return -1
            return choose(left, right)
        start = find_idx(lambda x : A[x] >= target, lambda x, y : x if A[x] == target else y)
        end = find_idx(lambda x : A[x] > target, lambda x, y : y if A[y] == target else x)
        if start == -1 or end == -1:
            return 0
        else:
            return end - start + 1
