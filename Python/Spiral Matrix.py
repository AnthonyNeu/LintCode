"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        if not matrix or not matrix[0]:
            return []
        result, top, bottom, left, right = [], 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            for i in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][i])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return result

class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        ret = []
        while matrix:
            # add the top row
            ret += matrix.pop(0)
            # add the right column
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            # add the bottom row
            if matrix:
                ret += matrix.pop()[::-1]
            # add the left column
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
