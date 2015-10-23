"""
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

    * Integers in each row are sorted from left to right.

    * Integers in each column are sorted from up to bottom.

    * No duplicate integers in each row or column.
"""

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        
        def searchMatrixHelper(left, top, right, bottom):
            if top > bottom or left > right:
                return 0
            if target < matrix[top][left] or target > matrix[bottom][right]:
                return 0
            mid, row, result = left + (right - left) / 2, top, 0
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    result += 1
                row +=1
            result += searchMatrixHelper(mid + 1, top, right, row - 1)
            result += searchMatrixHelper(left, row, mid - 1, bottom)
            return result
        return searchMatrixHelper(0, 0, n - 1, m - 1)
