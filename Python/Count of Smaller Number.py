"""
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query list. 
For each query, give you an integer, return the number of element in the array that are smaller than the given integer.

Example
For array [1,2,7,8,5], and queries [1,8,5], return [0,4,2]

Note
We suggest you finish problem Segment Tree Build and Segment Tree Query II first.

Challenge
Could you use three ways to do it.

Just loop
Sort and binary search
Build Segment Tree and Search.
"""


class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        if not A and queries:
            return [0] * len(queries)
        if not queries:
            return []
        A.sort()
        result = []
        def binary_search(num):
            left, right = 0, len(A) - 1
            while left + 1 < right:
                mid = left + (right - left) / 2
                if A[mid] >= num:
                    right = mid - 1
                else:
                    left = mid
            if A[right] < num:
                return right
            if A[left] < num:
                return left
            return -1
        for query in queries:
            result.append(binary_search(query) + 1)
        return result

# use segment tree
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None

class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        if not queries:
            return []
        if not A:
            return [0] * len(queries)
        min_A, max_A = min(A), max(A)
        segment_tree, result = self.build(min_A, max_A), []
        for i in range(len(A)):
            self.modify(segment_tree, A[i], 1)
        for query in queries:
            result.append(self.query(segment_tree, min_A, query - 1))
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
        left_sum, right_sum = 0, 0
        if start <= mid:
            if mid < end:
                left_sum = self.query(root.left, start, mid)
            else:
                left_sum = self.query(root.left, start, end)
        if mid < end:
            if start <= mid:
                right_sum = self.query(root.right, mid + 1, end)
            else:
                right_sum = self.query(root.right, start, end)
        return left_sum + right_sum

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
