"""
Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.

Example
Given 5*4 matrix

[12,13,0,12]
[13,4,13,12]
[13,8,10,12]
[12,13,12,12]
[13,13,13,13]
return 14.
"""

class Cell:
    def __init__(self, x, y, h):
        self.x, self.y, self.h = x, y, h
    
    def __cmp__(self, other):
        # min heap
        return self.h - other.h

class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        """
        Find the min height with no water that higher than the current height and keep it.
        Starting from the min height with no water
        """
        import heapq
        if not heights or len(heights) == 0 or len(heights[0]) == 0:
            return 0
        m, n = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap, visited = [], [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            heapq.heappush(heap, Cell(i, 0, heights[i][0]))
            heapq.heappush(heap, Cell(i, n - 1, heights[i][n - 1]))
            visited[i][0], visited[i][n - 1] = True, True
        for i in range(n):
            heapq.heappush(heap, Cell(0, i, heights[0][i]))
            heapq.heappush(heap, Cell(m - 1, i, heights[m - 1][i]))
            visited[0][i], visited[m - 1][i] = True, True
        result = 0
        while heap:
            cell = heapq.heappop(heap)
            x, y = cell.x, cell.y
            for i in range(4):
                nx, ny = x + directions[i][0], y + directions[i][1]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, Cell(nx, ny, max(cell.h, heights[nx][ny])))
                    result += max(0, cell.h - heights[nx][ny])
        return result
