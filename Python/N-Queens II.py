"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""

class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        self.column = [False] * n
        self.main_diag = [False] * 2 * n
        self.anti_diag = [False] * 2 * n
        
        def total_n_queens_helper(row):
            if row == n:
                return 1
            result = 0
            for i in range(n):
                if not self.column[i] and not self.main_diag[i + row] and not self.anti_diag[n + row - i]:
                    self.column[i] = self.main_diag[i + row] = self.anti_diag[n + row - i] = True
                    result += total_n_queens_helper(row + 1)
                    self.column[i] = self.main_diag[i + row] = self.anti_diag[n + row - i] = False
            return result
        return total_n_queens_helper(0)
