"""
Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. 
(The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)

Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.

Note
O(n) time and O(1) extra space.
"""

class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if not A or len(A) == 0:
            return 0
        cur_increase, cur_decrease = 1, 1
        max_increase, max_decrease = 0, 0
        for i in range(1, len(A)):
            if A[i] >= A[i - 1]:
                cur_increase += 1
            else:
                max_increase = max(cur_increase, max_increase)
                cur_increase = 1
        max_increase = max(cur_increase, max_increase)
        for i in range(len(A) - 1):
            if A[i] >= A[i + 1]:
                cur_decrease += 1
            else:
                max_decrease = max(cur_decrease, max_decrease)
                cur_decrease = 1
        max_decrease = max(cur_decrease, max_decrease)
        return max(max_increase, max_decrease)
