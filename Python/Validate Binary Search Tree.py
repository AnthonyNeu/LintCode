"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here

        def isValidBSTHelper(root, left, right):
            if root is None:
                return True
            if root.val <= left or root.val >= right:
                return False
            is_left_valid = True if root.left is None else isValidBSTHelper(root.left, left, root.val)
            is_right_valid = True if root.right is None else isValidBSTHelper(root.right, root.val, right)
            return is_left_valid and is_right_valid
        return isValidBSTHelper(root, float('-inf'), float('inf'))

class Solution(object):
    prev = None
    def isValidBST(self, root):

        def helper(root):
            if not root:
                return True
            if not helper(root.left):
                return False
            if self.prev and self.prev.val >= root.val:
                return False
            self.prev = root
            return helper(root.right)
        return helper(root)
