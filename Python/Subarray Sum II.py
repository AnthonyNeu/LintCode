"""
Given an integer array, find a subarray where the sum of numbers is between two given interval. Your code should return the number of possible answer. (The element in the array should be positive)

Have you met this question in a real interview? Yes
Example
Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:

[0, 0]
[0, 1]
[1, 1]
[2, 2]
"""

class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        # Write your code here
        n = len(A)
        cnt = 0
        sum_ending_at_i = [0 for _ in xrange(n+1)]

        for i in xrange(1, n+1):
            sum_ending_at_i[i] = sum_ending_at_i[i-1]+A[i-1]  # from left

        sum_ending_at_i.sort()
        for i in xrange(n + 1):
            # find the lowest and highest index for sum which is in range [start, end]
            lo = self.bisect_left(sum_ending_at_i, sum_ending_at_i[i] - end, 0, i)
            hi = self.bisect_right(sum_ending_at_i, sum_ending_at_i[i] - start, 0, i)
            cnt += hi-lo
        return cnt
        
    def bisect_left(self, A, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if A[mid] < x: lo = mid+1
            else: hi = mid
        return lo
        
    def bisect_right(self, A, x, lo, hi):
        while lo < hi:
            mid = (lo+hi)//2
            if x < A[mid]: hi = mid
            else: lo = mid+1
        return lo
