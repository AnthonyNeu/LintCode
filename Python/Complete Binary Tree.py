"""
Check a binary tree is completed or not. A complete binary tree is not binary tree that every level is completed filled except the deepest level. 
In the deepest level, all nodes must be as left as possible.

Example
    1
   / \
  2   3
 /
4
is a complete binary.

    1
   / \
  2   3
   \
    4
is not a complete binary.

Challenge
Do it in O(n) time
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
    @param root, the root of binary tree.
    @return true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):
        # Write your code here
        from collections import deque
        if not root:
            return True
        queue = deque([root])
        is_deepest = False
        while queue and not is_deepest:
            next_level = deque([])
            i, level = 0, len(queue)
            while i < level:
                node = queue.popleft()
                # cannot have a node has any children
                if is_deepest and (node.left or node.right):
                    return False
                if node.left and node.right:
                    next_level.append(node.left)
                    next_level.append(node.right)
                elif node.left and not node.right:
                    is_deepest = True
                    next_level.append(node.left)
                elif not node.left and node.right:
                    return False
                else:
                    is_deepest = True
                i += 1
            queue = next_level
            # check whether node in next_level has children
            if is_deepest:
                if next_level:
                    for child in next_level:
                        if child.left or child.right:
                            return False
                    return True
        return True
