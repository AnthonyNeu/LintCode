"""
Given a list of numbers, return all possible permutations.
"""

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None or not nums:
            return []
        result, length = [], len(nums)
        nums.sort()
        visited = [False] * length
        
        def permuteHelper(count, current):
            if count == length:
                result.append(list(current))
            for i in range(length):
                if visited[i]:
                    continue
                visited[i] = True
                current.append(nums[i])
                permuteHelper(count + 1, current)
                current.pop()
                visited[i] = False
        permuteHelper(0, [])
        return result
        