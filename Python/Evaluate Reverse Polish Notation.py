"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Example
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        # Write your code here
        stack = []
        for token in tokens:
            if not stack:
                stack.append(int(token))
            else:
                if token == '+':
                    stack.append(stack.pop() + stack.pop())
                elif token == '-':
                    stack.append(- stack.pop() + stack.pop())
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                elif token == '/':
                    stack.append(int(1 / float(stack.pop()) * float(stack.pop())))
                else:
                    stack.append(int(token))
        return int(stack[-1])
