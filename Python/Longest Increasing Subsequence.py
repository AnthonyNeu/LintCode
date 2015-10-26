"""
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.
"""
# O(n ^ 2)
class Solution1:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] <= nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if nums is not None and len(nums) > 0 else 0

# n log(n)
class Solution2:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        dp = []
        
        def insert(target):
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if dp[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(dp):
                dp.append(target)
            else:
                dp[left] = target
        for num in nums:
            insert(num)
        return len(dp)
