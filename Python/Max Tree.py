"""
Given an integer array with no duplicates. A max tree building on this array is defined as follow:

The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.

Have you met this question in a real interview? Yes
Example
Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:

    6
   / \
  5   3
 /   / \
2   0   1
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        if not A or len(A) == 0:
            return None
        # the stack store the nodes in descending order
        stack = [TreeNode(A[0])]
        for i in range(1, len(A)):
            if A[i] <= stack[-1].val:
                node = TreeNode(A[i])
                stack.append(node)
            # pop every node which value is less than A[i]
            # all let it as the right child of the last node which is less than A[i]
            else:
                smaller_node = stack.pop()
                while stack and stack[-1].val < A[i]:
                    stack[-1].right = smaller_node
                    smaller_node = stack.pop()
                    
                # pop the last node which value is less 
                # than A[i], and let it as the left child
                # and add A[i] to stack
                node = TreeNode(A[i])
                node.left = smaller_node
                stack.append(node)
        
        # pop all nodes in the stack and let them as the right child of root
        root = stack.pop()
        while stack:
            stack[-1].right = root
            root = stack.pop()
        return root
