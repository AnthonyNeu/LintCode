"""
Given a sorted (increasing order) array, Convert it to create a binary tree with minimal height.

Example
Given [1,2,3,4,5,6,7], return

     4
   /   \
  2     6
 / \    / \
1   3  5   7
Note
There may exist multiple valid solutions, return any of them.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        if not A:
            return None

        def helper(left, right):
            if left > right:
                return None
            mid = left + (right - left) / 2
            root = TreeNode(A[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(A) - 1)

# iterative solution
# https://leetcode.com/discuss/36616/java-iterative-solution
class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        from collections import deque
        if not A:
            return None
        length, root = len(A), TreeNode(-1)
        nodes, left_idx, right_idx = deque([root]), deque([0]), deque([length - 1])
        while nodes:
            node = nodes.popleft()
            left, right = left_idx.popleft(), right_idx.popleft()
            mid = left + (right - left) / 2
            node.val = A[mid]
            if left <= mid - 1:
                node.left = TreeNode(-1)
                nodes.append(node.left)
                left_idx.append(left)
                right_idx.append(mid - 1)
            if mid + 1 <= right:
                node.right = TreeNode(-1)
                nodes.append(node.right)
                left_idx.append(mid + 1)
                right_idx.append(right)
        return root
