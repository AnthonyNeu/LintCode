"""
There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.

Example
Given a matrix:

[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Note
The matrix may contains multiple peeks, find any of them.

Challenge
Solve it in O(n+m) time.

If you come up with an algorithm that you thought it is O(n log m) or O(m log n), can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?

T(m, n) = T(m, n / 2) + O(m) = T(m / 2, n / 2) + O(m) + O(n) = ... = O(m + n)
"""

class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        if not A:
            return [-1, -1]
        m, n = len(A), len(A[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left < right and top < bottom:
            if bottom - top < right - left:
                mid = left + (right - left) / 2
                c_max = float('-inf')
                i, j = -1, -1
                # find the max element in this column
                for p in range(top, bottom):
                    c_max = max(c_max, A[p][mid])
                    if c_max == A[p][mid]:
                        i, j = p, mid
                if A[i][j - 1] > c_max:
                    right = mid
                elif A[i][j + 1] > c_max:
                    left = mid + 1
                else:
                    return [i, j]
            else:
                mid = top + (bottom - top) / 2
                c_max = float('-inf')
                i, j = -1, -1
                # find the max element in this row
                for p in range(left, right):
                    c_max = max(c_max, A[mid][p])
                    if c_max == A[mid][p]:
                        i, j = mid, p
                if A[i - 1][j] > c_max:
                    bottom = mid
                elif A[i + 1][j] > c_max:
                    top = mid + 1
                else:
                    return [i, j]
        return [-1, -1]
