"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
Example
There exist two distinct solutions to the 4-queens puzzle:

[

    [".Q..", // Solution 1

     "...Q",

     "Q...",

     "..Q."],

    ["..Q.", // Solution 2

     "Q...",

     "...Q",

     ".Q.."]

]
"""

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.column = [False] * n
        self.main_diag = [False] * 2 * n
        self.anti_diag = [False] * 2 * n
        # record which column is taken in each row
        self.used = [-1] * n
        result = []
        
        def dfs(row):
            if row == n:
                # solution = [''.join(['Q' if self.used[i] == j else '.' for j in range(n)]) for i in range(n)]
                solution = []
                for i in range(n):
                    current_row = ['.'] * n
                    for j in range(n):
                        if self.used[i] == j:
                            current_row[j] = 'Q'
                    solution.append(''.join(current_row))
                result.append(solution)
            else:
                for i in range(n):
                    if not self.column[i] and not self.main_diag[i + row] and not self.anti_diag[n + row - i]:
                        self.used[row] = i
                        self.column[i] = self.main_diag[i + row] = self.anti_diag[n + row - i] = True
                        dfs(row + 1)
                        self.column[i] = self.main_diag[i + row] = self.anti_diag[n + row - i] = False
                        self.used[row] = -1
        dfs(0)
        return result
