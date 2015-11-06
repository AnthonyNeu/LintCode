"""
For an array, we can build a SegmentTree for it, each node stores an extra attribute count to denote the number of elements in the the array which value is between interval start and end. (The array may not fully filled by elements)

Design a query method with three parameters root, start and end, find the number of elements in the in array's interval [start, end] by the given root of value SegmentTree.

For array [0, 2, 3], the corresponding value Segment Tree is:

                     [0, 3, count=3]
                     /             \
          [0,1,count=1]             [2,3,count=2]
          /         \               /            \
   [0,0,count=1] [1,1,count=0] [2,2,count=1], [3,3,count=1]
query(1, 1), return 0

query(1, 2), return 1

query(2, 3), return 2

query(0, 2), return 2
"""

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The count number in the interval [start, end] 
    def query(self, root, start, end):
        # write your code here
        if start > end or not root:
            return 0
        if start <= root.start and root.end <= end:
            return root.count
        mid = root.start + (root.end - root.start) / 2
        left_count, right_count = 0, 0
        if start <= mid:
            if mid < end:
                left_count = self.query(root.left, start, mid)
            else:
                left_count = self.query(root.left, start, end)
        if mid < end:
            if start <= mid:
                right_count = self.query(root.right, mid + 1, end)
            else:
                right_count = self.query(root.right, start, end)
        return left_count + right_count

class Solution2: 

    def query(self, root, start, end):
        # write your code here
        if not root:
            return 0
        if start <= root.start and end >= root.end:
            return root.count
        mid = root.start + (root.end - root.start) / 2
        if mid >= end:
            return self.query(root.left, start, end)
        elif mid + 1 <= start:
            return self.query(root.right, start, end)
        else:
            return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)
