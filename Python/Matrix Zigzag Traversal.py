"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in ZigZag-order.

Example
Given a matrix:

[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]
return [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
"""

class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return []
        result, m, n, reverse = [], len(matrix), len(matrix[0]), True
        # follow the diagonal direction
        for k in range(m + n - 1):
            if k <= n - 1:
                x, y = 0, k
            else:
                x, y = k - n + 1, n - 1
            level = []
            while x <= m - 1 and y >= 0:
                level.append(matrix[x][y])
                x += 1
                y -= 1
            if reverse:
                result.extend(level[::-1])
            else:
                result.extend(level)
            reverse = not reverse
        return result
