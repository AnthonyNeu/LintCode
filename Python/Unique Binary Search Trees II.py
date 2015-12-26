"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

Example
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# This is not DP, as DP will use a lot of spaces and we also need
# to deep copy each subtree if using DP solution.
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here

        def helper(low, high):
            result = []
            if low > high:
                return [None]
            for i in range(low, high + 1):
                left = helper(low, i - 1)
                right = helper(i + 1, high)
                for j in left:
                    for k in right:
                        cur = TreeNode(i)
                        cur.left = j
                        cur.right = k
                        result.append(cur)
            return result
        return helper(1, n)
