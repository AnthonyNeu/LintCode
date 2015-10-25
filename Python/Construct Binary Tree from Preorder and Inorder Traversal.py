"""
Given preorder and inorder traversal of a tree, construct the binary tree.
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
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack, i, j = [root], 1, 0
        
        while True:
            if inorder[j] == stack[-1].val:
                p = stack.pop()
                j += 1
                if j == len(inorder): break
                if stack and stack[-1].val == inorder[j]: continue
                p.right = TreeNode(preorder[i])
                i += 1
                stack.append(p.right)
            else:
                p = TreeNode(preorder[i])
                i += 1
                stack[-1].left = p
                stack.append(p)
        return root
