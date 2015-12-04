"""
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Given a binary tree, and target = 5:

     1
    / \
   2   4
  / \
 2   3
return

[
  [1, 2, 2],
  [1, 4]
]
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        if not root:
            return []
        if not root.left and not root.right:
            return [] if root.val != target else [[root.val]]
        result = []
        for node in (root.left, root.right):
            if node:
                temp_result = self.binaryTreePathSum(node, target - root.val)
                for l in temp_result:
                    result.append([root.val] + l)
        return result
