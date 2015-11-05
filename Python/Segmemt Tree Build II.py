"""
The structure of Segment Tree is a binary tree which each node has two attributes start and end denote an segment / interval.

start and end are both integers, they should be assigned in following rules:

The root's start and end is given by build method.
The left child of node A has start=A.left, end=(A.left + A.right) / 2.
The right child of node A has start=(A.left + A.right) / 2 + 1, end=A.right.
if start equals to end, there will be no children for this node.
Implement a build method with a given array, so that we can create a corresponding segment tree with every node value represent the corresponding interval max value in the array, return the root of this segment tree.

Example
Given [3,2,1,4]. The segment tree will be:

                 [0,  3] (max = 4)
                  /            \
        [0,  1] (max = 3)     [2, 3]  (max = 4)
        /        \               /             \
[0, 0](max = 3)  [1, 1](max = 2)[2, 2](max = 1) [3, 3] (max = 4)
Clarification
Segment Tree (a.k.a Interval Tree) is an advanced data structure which can support queries like:

which of these intervals contain a given point
which of these points are in a given interval
See wiki: https://en.wikipedia.org/wiki/Interval_tree
https://en.wikipedia.org/wiki/Segment_tree
"""

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        if not A or len(A) == 0:
            return None
        
        def helper(start, end):
            if start > end:
                return None
            root = SegmentTreeNode(start, end, max(A[start:end + 1]))
            if len(A[start:end + 1]) != 1:
                mid = start + (end - start) / 2
                root.left = helper(start, mid)
                root.right = helper(mid + 1, end)
            return root
        return helper(0, len(A) - 1)
