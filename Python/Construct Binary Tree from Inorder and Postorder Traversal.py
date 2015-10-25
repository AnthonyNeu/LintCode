"""
Given inorder and postorder traversal of a tree, construct the binary tree.
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
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if len(inorder) == 0:
            return None
        root= TreeNode(postorder.pop())
        stack = [root]
        
        while stack:
            if stack[-1].val == inorder[-1]:
                p = stack.pop()
                inorder.pop()
                if len(inorder) == 0: break
                if stack and stack[-1].val == inorder[-1]: continue
                p.left = TreeNode(postorder.pop())
                stack.append(p.left)
            else:
                p = TreeNode(postorder.pop())
                stack[-1].right = p
                stack.append(p)
        return root
