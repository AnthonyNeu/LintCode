"""
Find K-th largest element in an array.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

Note
You can swap elements in the array

Challenge
O(n) time, O(1) extra memory.
"""

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        from random import randint
        left,right = 0, len(A) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = self.partition(left, right, pivot_idx, A)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx -1
            else:
                left = new_pivot_idx + 1
        
    def partition(self, left, right, pivot_idx, nums):
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        store_idx = left
        for i in xrange(left,right):
            # we want to get the bigger half, so we move the bigger element to the front
            if nums[i] > pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        return store_idx
