"""
Given an integer matrix, find a submatrix where the sum of numbers is zero.
Your code should return the coordinate of the left-up and right-down number.

Example
Given matrix

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
return [(1,1), (2,2)]

Challenge
O(n3) time.
"""

class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        m, n, result = len(matrix), len(matrix[0]), []
        for i in range(n):
            cur_sum = [0 for _ in range(m)]
            for j in range(i, n):
                # cur_sum[k] is the sum of subarray (k, i) to (k, j)
                for k in range(m):
                    cur_sum[k] += matrix[k][j]
                # apply the method of subarray sum
                # to find a submatrix with zero sum
                cache, last_sum = {}, 0
                # special case when total sum is 0
                cache[0] = -1
                for idx in range(0, m):
                    last_sum += cur_sum[idx]
                    if last_sum in cache:
                        result.append((cache[last_sum] + 1, i))
                        result.append((idx, j))
                        return result
                    cache[last_sum] = idx
        return result

class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        m, n, result = len(matrix), len(matrix[0]), []
        cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                cache[i + 1][j + 1] = matrix[i][j] + cache[i + 1][j] + cache[i][j + 1] - cache[i][j]
        for i in range(m):
            for j in range(i + 1, m + 1):
                sub_sum = {}
                for k in range(n + 1):
                    diff = cache[j][k] - cache[i][k]
                    if diff in sub_sum:
                        result.append((i, sub_sum[diff]))
                        result.append((j - 1, k - 1))
                        return result
                    sub_sum[diff] = k
        return result
