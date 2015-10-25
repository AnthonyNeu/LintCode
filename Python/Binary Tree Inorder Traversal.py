"""
Given a binary tree, return the inorder traversal of its nodes' values.
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        stack, inorder = [], []
        while stack or root is not None:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inorder.append(root.val)
                root = root.right
        return inorder
