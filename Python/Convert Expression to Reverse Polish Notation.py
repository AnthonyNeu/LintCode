"""
Given an expression string array, return the Reverse Polish notation of this expression. (remove the parentheses)

Example
For the expression [3 - 4 + 5] (which denote by ["3", "-", "4", "+", "5"]), return [3 4 - 5 +] (which denote by ["3", "4", "-", "5", "+"])
"""

class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
    def convertToRPN(self, expression):
        # write your code here
        if not expression or len(expression) == 0:
            return None
        ops, result = [], []
        for string in expression:
            if string.isdigit():
                result.append([string])
            else:
                if string == '(':
                    ops.append(string)
                elif string == '-' or string == '+':
                    while ops and ops[-1] != '(':
                        op = ops.pop()
                        right = result.pop()
                        left = result.pop()
                        result.append(left + right + [op])
                    ops.append(string)
                elif string == '*' or string == '/':
                    while ops and ops[-1] not in ('+', '(', '-'):
                        op = ops.pop()
                        right = result.pop()
                        left = result.pop()
                        result.append(left + right + [op])
                    ops.append(string)
                elif string == '(':
                    ops.append(string)
                else:
                    while ops and ops[-1] != '(':
                        op = ops.pop()
                        right = result.pop()
                        left = result.pop()
                        result.append(left + right + [op])
                    # pop the left bracket
                    ops.pop()
        while ops:
            op = ops.pop()
            right = result.pop()
            left = result.pop()
            result.append(left + right + [op])
        return result[0] if result else []      
