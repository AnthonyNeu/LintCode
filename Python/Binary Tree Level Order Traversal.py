"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# BFS
class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
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
        return result

# DFS
class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        result, self.max_level = [], 0
        while True:
            level = []

            def dfs(root, cur_level):
                if root is None or cur_level > self.max_level:
                    return
                if cur_level == self.max_level:
                    level.append(root.val)
                    return
                dfs(root.left, cur_level + 1)
                dfs(root.right, cur_level + 1)
            dfs(root, 0)
            if not level:
                break
            result.append(list(level))
            self.max_level += 1
        return result
