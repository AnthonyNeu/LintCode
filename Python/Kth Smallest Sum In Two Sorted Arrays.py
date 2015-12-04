"""
Given two integer arrays sorted in ascending order and an integer k. 
Define sum = a + b, where a is an element from the first array and b is an element from the second one. 
Find the kth smallest sum out of all possible sums.

Example
Given [1, 7, 11] and [2, 4, 6].

For k = 3, return 7.

For k = 4, return 9.

For k = 8, return 15.

Challenge
Do it in either of the following time complexity:

O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
O( (m + n) log maxValue). where maxValue is the max number in A and B.
"""

class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A or not B:
            return 0
        import heapq
        m, n = len(A), len(B)
        def vertical_search(k):
            heap = []
            for i in range(min(k, n)):
                heapq.heappush(heap, (A[0] + B[i], 0, i))
            while k > 1:
                min_element = heapq.heappop(heap)
                x, y = min_element[1], min_element[2]
                if x + 1 < m:
                    heapq.heappush(heap, (A[x + 1] + B[y], x + 1, y))
                k -= 1
            return heapq.heappop(heap)[0]
        return vertical_search(k)
