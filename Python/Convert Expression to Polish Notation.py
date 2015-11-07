"""
Given an expression string array, return the Polish notation of this expression. (remove the parentheses)

Example
For the expression [(5 − 6) * 7] (which represented by ["(", "5", "−", "6", ")", "*", "7"]), the corresponding polish notation is [* - 5 6 7] (which the return value should be ["*", "−", "5", "6", "7"]).

Clarification
Definition of Polish Notation:

http://en.wikipedia.org/wiki/Polish_notation
"""

class Solution:
    # @param expression: A string list
    # @return: The Polish notation of this expression
    def convertToPN(self, expression):
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
                        result.append([op] + left + right)
                    ops.append(string)
                elif string == '*' or string == '/':
                    while ops and ops[-1] not in ('+', '(', '-'):
                        op = ops.pop()
                        right = result.pop()
                        left = result.pop()
                        result.append([op] + left + right)
                    ops.append(string)
                elif string == '(':
                    ops.append(string)
                else:
                    while ops and ops[-1] != '(':
                        op = ops.pop()
                        right = result.pop()
                        left = result.pop()
                        result.append([op] + left + right)
                    # pop the left bracket
                    ops.pop()
        while ops:
            op = ops.pop()
            right = result.pop()
            left = result.pop()
            result.append([op] + left + right)
        return result[0] if result else []      
