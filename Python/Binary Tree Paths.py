"""
Given a binary tree, return all root-to-leaf paths.

Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
]
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        result = []
        if root.left:
            left = self.binaryTreePaths(root.left)
            result.extend([str(root.val) + '->' + path for path in left])
        if root.right:
            right = self.binaryTreePaths(root.right)
            result.extend([str(root.val) + '->' + path for path in right])
        return result
