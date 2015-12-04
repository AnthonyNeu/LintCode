"""
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. 
Otherwise, sorted in ascending order by number if the difference is same.

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.
"""

class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        length = len(A)
        def search_insertion_place():
            left, right = 0, length - 1
            while left + 1 < right:
                mid = left + (right - left) / 2
                if A[mid] > target:
                    right = mid
                else:
                    left = mid
            return left, right
        left, right = search_insertion_place()
        result = []
        while k > 0 and (left >= 0 or right < length):
            if left >= 0 and right < length:
                if abs(A[left] - target) <= abs(A[right] - target):
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1 
            elif right == length:
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
            k -= 1
        return result
