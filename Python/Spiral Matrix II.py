"""
Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example
Given n = 3,

You should return the following matrix:

[
  [ 1, 2, 3 ],
  [ 8, 9, 4 ],
  [ 7, 6, 5 ]
]
"""

class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        # Write your code here
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        idx = 1
        while idx <= n * n and left <= right and top <= bottom:
            for i in range(left,right + 1):
                matrix[top][i] = idx
                idx += 1
            for i in range(top + 1,bottom):
                matrix[i][right] = idx
                idx += 1
            for i in reversed(range(left, right + 1)):
                if idx <= n * n and top < bottom:
                    matrix[bottom][i] = idx
                    idx += 1
            for i in reversed(range(top + 1, bottom)):
                if idx <= n* n and left < right:
                    matrix[i][left] = idx
                    idx += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return matrix

class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        # Write your code here
        matrix = [[0] * n for _ in range(n)]
        # di, dj is the direction we need to go for the element
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(n*n):
            matrix[i][j] = k + 1
            # if we reach the end
            if matrix[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return matrix
