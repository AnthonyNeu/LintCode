"""
Given two array of integers(the first array is array A, the second array is array B), now we are going to find a element in array A which is A[i], and another element in array B which is B[j], so that the difference between A[i] and B[j] (|A[i] - B[j]|) is as small as possible, return their smallest difference.

Example
For example, given array A = [3,6,7,4], B = [2,8,9,3], return 0

Challenge
O(n log n) time
"""

# use binary search
class Solution1:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        # write your code here
        A.sort()
        B.sort()
        min_diff = float('inf')
        for num in B:
            min_diff = min(min_diff, abs(num - self.findSmaller(num, A)), abs(self.findLarger(num, A) - num))
        return min_diff
        
    def findSmaller(self, target, A):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return target
            elif A[mid] < target:
                left = mid
            else:
                right = mid
        return A[left] if abs(A[left] - target) <= abs(A[right] - target) else A[right]
    
    def findLarger(self, target, A):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return target
            elif A[mid] > target:
                right = mid
            else:
                left = mid
        return A[left] if abs(A[left] - target) <= abs(A[right] - target) else A[right]

# two pointers
class Solution2:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        # write your code here
        A.sort()
        B.sort()
        min_diff = float('inf')
        idx_A, idx_B = 0, 0
        while idx_A < len(A) and idx_B < len(B):
            while idx_B + 1 < len(B):
                if B[idx_B + 1] > A[idx_A]:
                    break
                idx_B += 1
            if idx_B < len(B):
                min_diff = min(min_diff, abs(B[idx_B] - A[idx_A]))
            if idx_B + 1 < len(B):
                min_diff = min(min_diff, abs(B[idx_B + 1] - A[idx_A]))
            idx_A += 1
        return min_diff
