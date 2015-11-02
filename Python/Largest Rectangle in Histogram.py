"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height or len(height) == 0:
            return 0
        stack, result = [], 0
        for i in range(len(height) + 1):
            # if we are at the last index, we must compute the max rectangle
            cur = -1 if i == len(height) else height[i]
            while stack and height[stack[-1]] >= cur:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        return result
