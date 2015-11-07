"""
Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;
"""

class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        from collections import deque
        q = deque()
        max_nums = []
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        for i in range(k, len(nums)):
            max_nums.append(nums[q[0]])
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q and q[0] <= i - k:
                q.popleft()
        if q:
            max_nums.append(nums[q[0]])
        return max_nums
