"""
Given a root of Binary Search Tree with unique value for each node.  
Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. 
You should keep the tree still a binary search tree after removal.

Example
Given binary search tree:

          5

       /    \

    3          6

 /    \

2       4

Remove 3, you can either return:

          5

       /    \

    2          6

      \

         4

or :

          5

       /    \

    4          6

 /   

2
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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    from: http://www.algolist.net/Data_structures/Binary_search_tree/Removal
    """    
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return None
        if root.val < value:
            root.right = self.removeNode(root.right, value)
            return root
        elif root.val > value:
            root.left = self.removeNode(root.left, value)
            return root
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            most_left = root.right
            """
            if cannot find the smallest node in right subtree
            just set the root left node to be the left of root.right 
            """
            if not most_left.left:
                most_left.left = root.left
                return most_left
            # find the smallest value in right subtree to replace current root
            while most_left.left:
                parent = most_left
                most_left = most_left.left
            parent.left = most_left.right
            most_left.left = root.left
            most_left.right = root.right
            return most_left
