"""
Given a list of numbers with duplicate number in it. Find all unique permutations.
"""

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        if nums is None or not nums:
            return []
        result, length = [], len(nums)
        nums.sort()
        visited = [False] * length
        
        def permuteHelper(count, current):
            if count == length:
                result.append(list(current))
            prev_idx = -1
            for i in range(length):
                if visited[i]:
                    continue
                if prev_idx != -1 and nums[prev_idx] == nums[i]:
                    continue
                visited[i] = True
                current.append(nums[i])
                permuteHelper(count + 1, current)
                current.pop()
                visited[i] = False
                prev_idx = i
        permuteHelper(0, [])
        return result
