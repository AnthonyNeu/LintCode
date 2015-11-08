"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Challenge
O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.
"""

# O(n) time and O(n) memory
class Solution1:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights or len(heights) == 0:
            return 0
        max_left = [0] * len(heights)
        max_right = [0] * len(heights)
        for i in range(1, len(heights)):
            max_left[i] = max(max_left[i - 1], heights[i - 1])
            max_right[- 1 - i] = max(max_right[- i], heights[- i])
        result = 0
        for i in range(len(heights)):
            h = min(max_left[i], max_right[i])
            if h > heights[i]:
                result += h - heights[i]
        return result

# O(n) time and O(n) memory using stack
class Solution2:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights or len(heights) == 0:
            return 0
        stack, result = [], 0
        for i in range(len(heights)):
            h = 0
            while stack:
                # pop all the elements in the stack which are smaller than height[i]
                bar, pos = stack[-1][0], stack[-1][1]
                result += (min(bar, heights[i]) - h) * (i - pos - 1)
                h = bar
                if heights[i] < bar:
                    break
                else:
                    stack.pop()
            stack.append((heights[i], i))
        return result

# O(n) time and O(1) memory
class Solution3:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights or len(heights) == 0:
            return 0
        n, max_length = len(heights), 0
        for i in range(len(heights)):
            if heights[max_length] < heights[i]:
                max_length = i
        water, peak = 0, 0
        for i in range(max_length):
            if heights[i] > peak:
                peak = heights[i]
            else:
                water += peak - heights[i]
        top = 0
        for i in reversed(range(max_length, len(heights))):
            if heights[i] > top:
                top = heights[i]
            else:
                water += top - heights[i]
        return water
