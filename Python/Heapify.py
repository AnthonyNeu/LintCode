"""
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
"""

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        length = len(A)
        
        def sift_down(i):
            left, right, largest = 2 * i + 1, 2 * i + 2, i
            if left < length and A[left] < A[largest]:
                largest = left
            if right < length and A[right] < A[largest]:
                largest = right
            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                sift_down(largest)
        for i in reversed(range(length / 2)):
            sift_down(i)
