"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
"""

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        length = len(A) + len(B)

        def find_k_th(A_start, B_start, k):
            if A_start >= len(A):
                return B[B_start + k - 1]
            if B_start >= len(B):
                return A[A_start + k - 1]
            if k == 1:
                return min(A[A_start], B[B_start])
            if A_start + k / 2 - 1 >= len(A):
                A_key = float('inf')
            else:
                A_key = A[A_start + k / 2 - 1]
            if B_start + k / 2 - 1 >= len(B):
                B_key = float('inf')
            else:
                B_key = B[B_start + k / 2 - 1]
            if A_key > B_key:
                return find_k_th(A_start, B_start + k / 2, k - k / 2)
            else:
                return find_k_th(A_start + k / 2, B_start, k - k / 2)
        if length % 2 == 0:
            return (find_k_th(0, 0, length / 2) + find_k_th(0, 0, length / 2 + 1)) / 2.0
        else:
            return find_k_th(0, 0, length / 2 + 1)
