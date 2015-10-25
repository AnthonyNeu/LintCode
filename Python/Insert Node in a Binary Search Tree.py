"""
Given a binary search tree and a new tree node, insert the node into the tree. 
You should keep the tree still be a valid binary search tree.
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
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        prev, cur = None, root
        while cur:
            prev = cur
            if cur.val > node.val:
                cur = cur.left
            else:
                cur = cur.right
        if prev is None:
            return node
        elif prev.val > node.val:
            prev.left = node
        else:
            prev.right = node
        return root
