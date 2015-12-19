"""
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
"""

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A or not B:
            return A or B
        idx1, idx2, result = 0, 0, []
        while idx1 < len(A) and idx2 < len(B):
            if A[idx1] < B[idx2]:
                result.append(A[idx1])
                idx1 += 1
            else:
                result.append(B[idx2])
                idx2 += 1
        if idx1 < len(A):
            result.extend(A[idx1:])
        elif idx2 < len(B):
            result.extend(B[idx2:])
        return result
