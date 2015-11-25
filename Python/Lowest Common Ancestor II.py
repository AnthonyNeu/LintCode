"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

The node has an extra attribute parent which point to the father of itself. The root's parent is null.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
"""

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        this.val = val
        this.parent, this.left, this.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """ 
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        if root in (None, A, B):
            return root
        left, right = [self.lowestCommonAncestorII(child, A, B) for child in (root.left, root.right)]
        # if both A and B in one of the subtree of root
        # then return LCA of that subtree
        # if A and B in different subtree
        # return this root
        # if neither of A or B in that subtree
        # return None
        return root if left and right else left or right
