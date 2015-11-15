"""
The structure of Expression Tree is a binary tree to evaluate certain expressions. All leaves of the Expression Tree have an number string value. All non-leaves of the Expression Tree have an operator string value.

Now, given an expression array, build the expression tree of this expression, return the root of this expression tree.

For the expression (2*6-(23+7)/(1+2)) (which can be represented by ["2" "*" "6" "-" "(" "23" "+" "7" ")" "/" "(" "1" "+" "2" ")"]). The expression tree will be like

                 [ - ]
             /          \
        [ * ]              [ / ]
      /     \           /         \
    [ 2 ]  [ 6 ]      [ + ]        [ + ]
                     /    \       /      \
                   [ 23 ][ 7 ] [ 1 ]   [ 2 ] .
After building the tree, you just need to return root node [-].
"""

"""
Definition of ExpressionTreeNode:
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None
"""


class Solution:
    # @param expression: A string list
    # @return: The root of expression tree
    def build(self, expression):
        # write your code here
        if not expression or len(expression) == 0:
            return None
        ops, nums = [], []
        for string in expression:
            if string.isdigit():
                etn = ExpressionTreeNode(string)
                nums.append(etn)
            else:
                if string == '(':
                    ops.append(ExpressionTreeNode(string))
                elif string == '-' or string == '+':
                    while ops and ops[-1].symbol != '(':
                        op = ops.pop()
                        op.right = nums.pop()
                        op.left = nums.pop()
                        nums.append(op)
                    ops.append(ExpressionTreeNode(string))
                elif string == '*' or string == '/':
                    while ops and ops[-1].symbol not in ('+', '(', '-'):
                        op = ops.pop()
                        op.right = nums.pop()
                        op.left = nums.pop()
                        nums.append(op)
                    ops.append(ExpressionTreeNode(string))
                else:
                    while ops and ops[-1].symbol != '(':
                        op = ops.pop()
                        op.right = nums.pop()
                        op.left = nums.pop()
                        nums.append(op)
                    # pop the left bracket
                    ops.pop()
        while ops:
            op = ops.pop()
            op.right = nums.pop()
            op.left = nums.pop()
            nums.append(op)
        return nums[0] if nums else None
