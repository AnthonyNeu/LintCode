"""
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Example
Given [-1, -2, -3, 4, 5, 6], after re-range, it will be [-1, 5, -2, 4, -3, 6] or any other reasonable answer.

Note
You are not necessary to keep the original order of positive integers or negative integers.

Challenge
Do it in-place and without extra memory.
"""

class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        # write your code here
        n, positive, expected_positive = len(A), 0, False
        positive = sum([1 if A[i] > 0 else 0 for i in range(n)])
        if 2 * positive > n:
            expected_positive = True
        # pos is the index of next positive number
        # neg is the index of next negative number
        pos, neg, i = 0, 0, 0
        while pos < n and neg < n:
            # find next positive number
            while pos < n and A[pos] < 0:
                pos += 1
            # find next negative number
            while neg < n and A[neg] > 0:
                neg += 1
            if expected_positive and A[i] < 0:
                A[i], A[pos] = A[pos], A[i]
            elif not expected_positive and A[i] > 0:
                A[i], A[neg] = A[neg], A[i]
            if i == pos:
                pos += 1
            if i == neg:
                neg += 1
            expected_positive = not expected_positive  
            i += 1
