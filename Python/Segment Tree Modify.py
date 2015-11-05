"""
Example
For segment tree:

                      [1, 4, max=3]
                    /                \
        [1, 2, max=2]                [3, 4, max=3]
       /              \             /             \
[1, 1, max=2], [2, 2, max=1], [3, 3, max=0], [4, 4, max=3]
if call modify(root, 2, 4), we can get:

                      [1, 4, max=4]
                    /                \
        [1, 2, max=4]                [3, 4, max=3]
       /              \             /             \
[1, 1, max=2], [2, 2, max=4], [3, 3, max=0], [4, 4, max=3]
or call modify(root, 4, 0), we can get:

                      [1, 4, max=2]
                    /                \
        [1, 2, max=2]                [3, 4, max=0]
       /              \             /             \
[1, 1, max=2], [2, 2, max=1], [3, 3, max=0], [4, 4, max=0]
"""

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    """
    @param root, index, value: The root of segment tree and 
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        if root.start == index and root.end == index:
            root.max = value
            return
        mid = root.start + (root.end - root.start) /2
        if index >= root.start and index <= mid:
            self.modify(root.left, index, value)
        elif index >= mid + 1 and index <= root.end:
            self.modify(root.right, index, value)
        root.max = max(root.left.max, root.right.max)
