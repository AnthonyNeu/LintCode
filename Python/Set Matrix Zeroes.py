"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Example
Given a matrix

[
  [1,2],
  [0,3]
],
return
[
[0,2],
[0,0]
]

Challenge
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return
        first_row_has_zero = False
        first_col_has_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_row_has_zero = True
                break
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_col_has_zero = True
                break
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_col_has_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
# https://leetcode.com/discuss/15997/any-shortest-o-1-space-solution
class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return
        first_col_has_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # Note the 'reverse' here as we cannot modify the matrix[0][j] on the upside down order
        for i in reversed(range(len(matrix))):
            for j in reversed(range(1, len(matrix[0]))):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if first_col_has_zero:
                matrix[i][0]  = 0
