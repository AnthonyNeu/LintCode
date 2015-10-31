"""
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
"""

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors or len(colors) == 0:
            return
        count, start, end = 0, 0, len(colors) - 1
        while count < k and start <= end:
            min_value, max_value = min(colors[start:end + 1]), max(colors[start:end + 1])
            left, right, idx = start, end, start
            while idx <= right:
                if colors[idx] == min_value:
                    colors[idx], colors[left] = colors[left], colors[idx]
                    left, idx = left + 1, idx + 1
                elif colors[idx] == max_value:
                    colors[idx], colors[right] = colors[right], colors[idx]
                    right = right - 1
                else:
                    idx += 1
            count += 2
            start, end = left, right
