"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
#Two-pass solution
class Solution1:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        H, W, M, N= 0, 1, len(matrix), len(matrix[0])
        # DP table stores (h, w) for each (i, j).
        table = [[(0, 0) for _ in range(N)] for _ in range(M)]
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                # Find the largest h such that (i, j) to (i + h - 1, j) are feasible.
                # Find the largest w such that (i, j) to (i, j + w - 1) are feasible.
                if matrix[i][j] == 1:
                    h, w = 1, 1
                    if i + 1 < M:
                        h = table[i + 1][j][H] + 1
                    if j + 1 < N:
                        w = table[i][j + 1][W] + 1
                    table[i][j] = (h, w)
        # A table stores the length of largest square for each (i, j).
        dp = [[0 for _ in range(N)] for _ in range(M)]
        max_area = 0
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if matrix[i][j] == 1:
                    side = min(table[i][j][H], table[i][j][W])
                    # Get the length of largest square with bottom-left corner (i, j).
                    if i + 1 < M and j + 1 < N:
                        side = min(dp[i + 1][j + 1] + 1, side)
                    dp[i][j] = side
                    max_area = max(max_area, side * side)
        return max_area

# one-pass solution
class Solution2:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        # for height, width, side of square
        H, W, S = 0, 1, 2
        M, N = len(matrix), len(matrix[0])
        dp = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(M + 1)]
        max_area = 0
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j][H] = dp[i - 1][j][H] + 1
                    dp[i][j][W] = dp[i][j - 1][W] + 1
                    dp[i][j][S] = min(dp[i - 1][j - 1][S] + 1, dp[i][j][H], dp[i][j][W])
                    max_area = max(max_area, dp[i][j][S] * dp[i][j][S])
        return max_area
