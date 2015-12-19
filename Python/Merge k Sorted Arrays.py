"""
Given k sorted integer arrays, merge them into one sorted array.

Example
Given 3 sorted arrays:

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

Challenge
Do it in O(N log k).

N is the total number of integers.
k is the number of arrays.
"""

class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        # Write your code here
        from heapq import heappush, heappop
        heap, result = [], []
        for i in range(len(arrays)):
            if arrays[i]:
                heappush(heap, (arrays[i][0], 0, i))
        while heap:
            x, idx, num = heap[0]
            heappop(heap)
            if idx < len(arrays[num]) - 1:
                heappush(heap, (arrays[num][idx + 1], idx + 1, num))
            result.append(x)
        return result
