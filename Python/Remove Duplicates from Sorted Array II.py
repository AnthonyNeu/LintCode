"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        start, end, state = 0, 1, 0
        while end < len(A):
            if A[start] == A[end]:
                if state == 0:
                    state = 1
                    start += 1
                    A[start] = A[end]
            else:
                state = 0
                start += 1
                A[start] = A[end]
            end += 1
        return start + 1

class Solution(object):
    def removeDuplicates(self, nums):
        """
        for this solution, we can change 2 to k for the problem which allows k duplicates.
        """
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i
