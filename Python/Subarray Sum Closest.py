"""
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if len(nums) == 1:
            return [0, 0]
        table, sum_list, length, cur = collections.defaultdict(list), [], len(nums), 0
        # same as Subarray Sum, we store the sum until current idx
        # also store the sum into a list
        for i, num in enumerate(nums):
            cur += num
            table[cur].append(i)
            sum_list.append(cur)
        sum_list.sort()
        gap = map(lambda x, y : abs(x - y), sum_list[:length - 1], sum_list[1:])
        min_gap = min(gap)
        # find the subarray which added up to the min gap
        for i in range(1, length):
            if abs(sum_list[i] - sum_list[i - 1]) == min_gap:
                if min_gap == 0:
                    return [table[sum_list[i]][0] + 1, table[sum_list[i]][1]]
                else:
                    min_idx = min(table[sum_list[i]][0], table[sum_list[i - 1]][0])
                    max_idx = max(table[sum_list[i]][0], table[sum_list[i - 1]][0])
                    return [min_idx + 1, max_idx]
