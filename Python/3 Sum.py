"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        numbers.sort()
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                if left > i + 1 and numbers[left] == numbers[left - 1]:
                    left += 1
                    continue
                if right < len(numbers) - 1 and numbers[right] == numbers[right + 1]:
                    right -= 1
                    continue
                three_sum = numbers[i] + numbers[left] + numbers[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([numbers[i], numbers[left], numbers[right]])
                    left, right = left + 1, right - 1
        return result
