"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).
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
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        if not root:
            return []
        queue, result = [], []
        queue.append(root)
        while queue:
            start, cur = None, []
            while queue and queue[0] != start:
                node = queue.pop(0)
                cur.append(node.val)
                if start is None and (node.left or node.right):
                    start = node.left if node.left else node.right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(cur))
        return result[::-1]
