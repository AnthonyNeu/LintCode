"""
Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. 
Each query has two integers [start, end]. 
For each query, calculate the sum number between index start and end in the given array, return the result list.

Example
For array [1,2,7,8,5], and queries [(0,4),(1,2),(2,4)], return [23,9,20]

Note
We suggest you finish problem Segment Tree Build, Segment Tree Query and Segment Tree Modify first.

Challenge
O(logN) time for each query
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        segment_tree_root = self._build(0, len(A) - 1, A)
        result = []
        for query in queries:
            start, end = query.start, query.end
            result.append(self._query(segment_tree_root, start, end))
        return result

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
