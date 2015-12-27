"""
Determine whether a Sudoku is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character ..
"""

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        visited = [False for _ in range(9)]

        def check(c):
            if c == '.':
                return True
            num = ord(c) - ord('0')
            if num < 1 or num > 9 or visited[num - 1]:
                return False
            visited[num - 1] = True
            return True
        for i in range(9):
            visited = [False] * 9
            for j in range(9):
                if check(board[i][j]) is False:
                    return False
        for i in range(9):
            visited = [False] * 9
            for j in range(9):
                if check(board[j][i]) is False:
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = [False] * 9
                for k in range(9):
                    if check(board[i + k / 3][j + k % 3]) is False:
                        return False
        return True
