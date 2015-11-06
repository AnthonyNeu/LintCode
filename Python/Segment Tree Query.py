"""
For an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end).

Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by the given root of segment tree.

Example
For array [1, 4, 2, 3], the corresponding Segment Tree is:

                  [0, 3, max=4]
                 /             \
          [0,1,max=4]        [2,3,max=3]
          /         \        /         \
   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
query(root, 1, 1), return 4

query(root, 1, 2), return 4

query(root, 2, 3), return 3

query(root, 0, 2), return 4
"""

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        # write your code here
        if not root:
            return float('-inf')
        if root.start >= start and end >= root.end:
            return root.max
        mid = root.start + (root.end - root.start) / 2
        if mid >= end:
            return self.query(root.left, start, end)
        elif mid + 1 <= start:
            return self.query(root.right, start, end)
        else:
            return max(self.query(root.left, start, mid), self.query(root.right, mid + 1, end))

class Solution2: 
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        # write your code here
        if not root or start > end:
            return float('-inf')
        if start <= root.start and root.end <= end:
            return root.max
        mid = root.start + (root.end - root.start) / 2
        left_max, right_max = float('-inf'), float('-inf')
        if start <= mid:
            if mid < end:
                left_max = self.query(root.left, start, mid)
            else:
                left_max = self.query(root.left, start, end)
        if mid < end:
            if start <= mid:
                right_max = self.query(root.right, mid + 1, end)
            else:
                right_max = self.query(root.right, start, end)
        return max(left_max, right_max)
