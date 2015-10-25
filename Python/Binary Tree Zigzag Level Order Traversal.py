"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).
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
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        queue, result = [], []
        queue.append(root)
        reverse = 0
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
            result.append(list(cur[::-1]) if reverse else list(cur))
            reverse = 1 - reverse
        return result
