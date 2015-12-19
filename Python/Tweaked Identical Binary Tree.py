"""
Check two given binary trees are identical or not. 
Assuming any number of tweaks are allowed. A tweak is defined as a swap of the children of one node in the tree.

Example
    1             1
   / \           / \
  2   3   and   3   2
 /                   \
4                     4
are identical.

    1             1
   / \           / \
  2   3   and   3   4
 /                   \
4                     2
are not identical.

Note
There is no two nodes with the same value in the tree.

Challenge
O(n) time
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        # Write your code here
        if a is None and b is None:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return (self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right)) or (self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left))
