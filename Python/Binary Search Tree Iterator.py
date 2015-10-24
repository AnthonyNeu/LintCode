"""
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
# Extra memory usage O(h), h is the height of the tree.
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
            
    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0
        
    #@return: return next node
    def next(self):
        #write your code here
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node
        