"""
Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example
    1
   / \
  2   2
 / \ / \
3  4 4  3
is a symmetric binary tree.

    1
   / \
  2   2
   \   \
   3    3
is not a symmetric binary tree.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution1:
    """
    @param root, the root of binary tree.
    @return true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # Write your code here
        
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        return True if not root else helper(root.left, root.right)

class Solution2:
    """
    @param root, the root of binary tree.
    @return true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p, q = stack.pop(), stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)
        return True
