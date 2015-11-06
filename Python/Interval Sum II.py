"""
Given an integer array in the construct method, implement two methods query(start, end) and modify(index, value):

For query(start, end), return the sum from index start to index end in the given array.
For modify(index, value), modify the number in the given index to value

Example
Given array A = [1,2,7,8,5].

query(0, 2), return 10.
modify(0, 4), change A[0] from 1 to 4.
query(0, 1), return 6.
modify(2, 1), change A[2] from 7 to 1.
query(2, 4), return 14.
"""

"""
class SegmentTreeNode:
    def __init__(self, start, sum):
        self.start, self.end, self.sum = start, end, sum
        self.left, self.right = None, None
"""

class Solution:	
    
    # @param A: An integer list
    def __init__(self, A):
        # write your code here
        self.root = self._build(0, len(A) - 1, A)

    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        # write your code here
        return self._query(self.root, start, end)

    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        # write your code here
        return self._modify(self.root, index, value)
        
    def _build(self, start, end, A):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, 0)
        if start != end:
            mid = start + (end - start) / 2
            root.left = self._build(start, mid, A)
            root.right = self._build(mid + 1, end, A)
            root.sum = root.left.sum + root.right.sum
        else:
            root.sum = A[start]
        return root

    def _query(self, root, start, end):
        if start > end or not root:
            return 0
        if start <= root.start and root.end <= end:
            return root.sum
        mid = root.start + (root.end - root.start) / 2
        left_sum, right_sum = 0, 0
        if start <= mid:
            if mid < end:
                left_sum = self._query(root.left, start, mid)
            else:
                left_sum = self._query(root.left, start, end)
        if mid < end:
            if start <= mid:
                right_sum = self._query(root.right, mid + 1, end)
            else:
                right_sum = self._query(root.right, start, end)
        return left_sum + right_sum
        
    def _modify(self, root, index, value):
        # write your code here
        if root.start == index and root.end == index:
            root.sum = value
            return
        mid = root.start + (root.end - root.start) /2
        if index >= root.start and index <= mid:
            self._modify(root.left, index, value)
        elif index >= mid + 1 and index <= root.end:
            self._modify(root.right, index, value)
        root.sum = root.left.sum + root.right.sum
