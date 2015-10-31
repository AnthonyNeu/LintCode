"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.
"""

class Solution1:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        # write your code here
        result, length = [], len(numbers)
        numbers.sort()
        for i in range(length):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                search_target, left, right = target - numbers[i] - numbers[j], j + 1, length - 1
                while left < right:
                    if left > j + 1 and numbers[left] == numbers[left - 1]:
                        left += 1
                        continue
                    if right < length - 1 and numbers[right] == numbers[right + 1]:
                        right -= 1
                        continue
                    if numbers[left] + numbers[right] == search_target:
                        result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left, right = left + 1, right - 1
                    elif numbers[left] + numbers[right] > search_target:
                        right -= 1
                    else:
                        left += 1
        return result

# change it to a 2Sum, but will lead to TLE
class Solution2:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        # write your code here
        from collections import defaultdict
        nums, result, lookup = sorted(numbers), [], defaultdict(list)
        for i in xrange(0, len(numbers) - 1):
            for j in xrange(i + 1, len(numbers)): 
                lookup[numbers[i] + numbers[j]].append([i, j])
        for key in lookup:
            if target - key in lookup:
                for x in lookup[key]:
                    for y in lookup[target - key]:
                        [a, b], [c, d] = x, y
                        if a is not c and b is not d and a is not d and b is not c:
                            quad = sorted([numbers[a], numbers[b], numbers[c], numbers[d]])
                            if quad not in result:
                                result.append(quad)
        return result
