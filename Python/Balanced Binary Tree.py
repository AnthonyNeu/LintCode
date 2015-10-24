"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution1:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
        
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

class Solution2:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.isBalancedHepler(root)

    def isBalancedHepler(self, root):
        if root is None:
            return True
        if self.get_height(root) == -1:
            return False
        return True

    def get_height(self, root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
