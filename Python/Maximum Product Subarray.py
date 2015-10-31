"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
"""

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        global_max, local_max, local_min = float('-inf'), 1, 1
        for num in nums:
            local_max = max(1, local_max)
            if num > 0:
                local_max, local_min = num * local_max, num * local_min
            else:
                local_max, local_min = num * local_min, num * local_max
            global_max = max(global_max, local_max)
        return global_max
