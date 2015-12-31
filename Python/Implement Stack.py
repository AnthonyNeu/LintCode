"""
Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

Example
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
"""

"""
class ListNode:
    def __init__(self, val):
        self.val, self.prev = val, None
"""

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self._top = None
        self.length = 0

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        if not self.top:
            self._top = ListNode(x)
        else:
            node = ListNode(x)
            node.prev = self._top
            self._top = node
        self.length += 1

    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        self._top = self._top.prev
        self.length -= 1

    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        return self._top.val

    # @return a boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return self.length == 0
