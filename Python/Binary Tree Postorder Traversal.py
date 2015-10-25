"""
Given a binary tree, return the postorder traversal of its nodes' values.
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        stack, postorder,cur, subtree_root = [], [], root, None
        while stack or cur is not None:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                peek_node = stack[-1]
                if peek_node.right != None and subtree_root != peek_node.right:
                    cur = peek_node.right
                else:
                    postorder.append(peek_node.val)
                    subtree_root = peek_node
                    stack.pop()
        return postorder
        