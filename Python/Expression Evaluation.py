"""
Given an expression string array, return the final result of this expression

Example
For the expression 2*6-(23+7)/(1+2), input is

[
  "2", "*", "6", "-", "(",
  "23", "+", "7", ")", "/",
  (", "1", "+", "2", ")"
],
return 2
"""

class Solution:
    # @param expression: a list of strings;
    # @return: an integer
    def evaluateExpression(self, expression):
        # write your code here
        rpn = self.convertToRPN(expression)
        if not rpn:
            return 0
        return self.evalRPN(rpn)

    def convertToRPN(self, expression):
        # write your code here
        if not expression or len(expression) == 0:
            return []
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

    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if len(stack) == 0:
                stack.append(token)
            else:
                if token is "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif token is "-":
                    stack.append(- int(stack.pop()) + int(stack.pop()))
                elif token is "/":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(int(num2 / num1))
                elif token is "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    stack.append(token)
        return int(stack.pop())
