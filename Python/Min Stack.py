"""
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.
"""

class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.min_value = None

    def push(self, number):
        # write your code here
        if not self.stack:
            self.min_value = number
            self.stack.append(0)
        else:
            self.stack.append(number - self.min_value)
            if self.min_value > number:
                self.min_value = number

    def pop(self):
        # pop and return the top item in stack
        value, element = self.stack.pop(), 0
        if value < 0:
            element = self.min_value
            self.min_value -= value
        else:
            element = self.min_value + value
        return element

    def min(self):
        # return the minimum number in stack
        return self.min_value
