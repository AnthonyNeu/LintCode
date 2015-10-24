"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root in (None, A, B):
            return root
        
        left, right = [self.lowestCommonAncestor(child, A, B) for child in (root.left, root.right)]
        
        return root if left and right else left or right
