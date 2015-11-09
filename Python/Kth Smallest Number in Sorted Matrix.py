"""
Find the kth smallest number in at row and column sorted matrix.

Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5
"""

class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        import heapq
        m, n = len(matrix), len(matrix[0])
        def vertical_search(k):
            heap = []
            for i in range(min(k, n)):
                heapq.heappush(heap, (matrix[0][i], 0, i))
            while k > 1:
                min_element = heapq.heappop(heap)
                x, y = min_element[1], min_element[2]
                if x + 1 < m:
                    heapq.heappush(heap, (matrix[x + 1][y], x + 1, y))
                k -=1
            return heapq.heappop(heap)[0]
        return vertical_search(k)
