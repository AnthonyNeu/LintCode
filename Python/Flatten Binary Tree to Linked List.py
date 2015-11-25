"""
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.


Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here

        def helper(root, head):
            if root:
                head = helper(root.right, head)
                head = helper(root.left, head)
                root.right = head
                root.left = None
                return root
            else:
                return head
        return helper(root, None)

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        while root:
            if root.left:
                head = root.left
                while head.right:
                    head = head.right
                head.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
