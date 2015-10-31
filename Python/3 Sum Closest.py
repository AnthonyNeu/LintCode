"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        result = float('inf')
        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                three_sum = numbers[i] + numbers[left] + numbers[right]
                if three_sum > target:
                    right -= 1
                elif three_sum < target:
                    left += 1
                else:
                    return target
                result =  three_sum if abs(three_sum - target) < abs(result - target) else result
        return result
