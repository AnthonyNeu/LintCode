"""
Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two integers [start, end]. 
For each query, calculate the minimum number between index start and end in the given array, return the result list.

Example
For array [1,2,7,8,5], and queries [(1,2),(0,4),(2,4)], return [2,1,5]
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
    def intervalMinNumber(self, A, queries):
        # write your code here
        segment_tree = self.build(0, len(A) - 1, A)
        answer = []
        for query in queries:
            answer.append(self.query(segment_tree, query.start, query.end))
        return answer
        
    def build(self, start, end, A):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, float('inf'))
        if start != end:
            mid = start + (end - start) / 2
            root.left = self.build(start, mid, A)
            root.right = self.build(mid + 1, end, A)
            root.min = min(root.left.min, root.right.min)
        else:
            root.min = A[start]
        return root

    def query(self, root, start, end):
        # write your code here
        if not root:
            return float('-inf')
        if start == root.start and end == root.end:
            return root.min
        mid = root.start + (root.end - root.start) / 2
        if mid >= end:
            return self.query(root.left, start, end)
        elif mid + 1 <= start:
            return self.query(root.right, start, end)
        else:
            return min(self.query(root.left, start, mid), self.query(root.right, mid + 1, end))
