"""
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) . 
For each element Ai in the array, count the number of element before this element Ai is smaller than it and return count number array.

Example:
For array [1,2,7,8,5], return [0,1,2,3,2]
"""

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end, self.count = start, end, 0
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        if not A or len(A) == 0:
            return []
        segment_tree, result = self.build(0, 10000), []
        for i in range(len(A)):
            answer = 0
            if A[i] > 0:
                answer = self.query(segment_tree, 0, A[i] - 1)
            result.append(answer)
            self.modify(segment_tree, A[i], 1)
        return result

    def build(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, 0)
        if start != end:
            mid = start + (end - start) / 2
            root.left = self.build(start, mid)
            root.right = self.build(mid + 1, end)
        else:
            root.count = 0
        return root

    def query(self, root, start, end):
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
    
    # add value to the index    
    def modify(self, root, index, value):
        # write your code here
        if root.start == index and root.end == index:
            root.count += value
            return
        mid = root.start + (root.end - root.start) /2
        if index >= root.start and index <= mid:
            self.modify(root.left, index, value)
        elif index >= mid + 1 and index <= root.end:
            self.modify(root.right, index, value)
        root.count = root.left.count + root.right.count
