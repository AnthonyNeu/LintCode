"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.
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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        if not root:
            return 0
        self.result = float('-inf')
        
        def maxPathSumHelper(root):
            if not root:
                return 0
            l, r =  max(0, maxPathSumHelper(root.left)), max(0, maxPathSumHelper(root.right))
            self.result = max(self.result, l + r + root.val)
            return max(l, r) + root.val
        maxPathSumHelper(root)
        return self.result
