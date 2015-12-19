"""
Sort a stack in ascending order (with biggest terms on top).

You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (e.g. array).

Example
Given stack =

| |
|3|
|1|
|2|
|4|
 -
return:

| |
|4|
|3|
|2|
|1|
 -
The data will be serialized to [4,2,1,3]. The last element is the element on the top of the stack.

Challenge
O(n^2) time is acceptable.
"""

#Your can use Stack class in your solution.
#class Stack:
#  def __init__(self, stk=[])
#    # use stk to initialize the stack
#  def isEmpty(self)
#    # return true is stack is empty or false/
#  def push(self, item)
#    # push a element into stack and return nothing
#  def pop(self)
#    # pop a element from stack
#  def peek(self):
#    # return the top element if stack is not empty or nothing
#  def size(self):
#    # return the size of stack
class Solution:
    # @param {Stack} stk an integer Stack
    # @return {int} void
    def stackSorting(self, stk):
        # Write your code here
        if not stk or stk.isEmpty():
            return
        stack = Stack()
        stack.push(stk.peek())
        stack.pop()
        while True:
            if stk.isEmpty():
                break
            # move the element smaller than the top of helper stack to helper stack
            while not stk.isEmpty() and stk.peek() <= stack.peek():
                stack.push(stk.peek())
                stk.pop()
            if not stk.isEmpty():
                # the element to insert in this loop
                elem = stk.peek()
                stk.pop()
                while not stack.isEmpty() and stack.peek() <= elem:
                    stk.push(stack.peek())
                    stack.pop()
                stack.push(elem)
                while not stk.isEmpty() and stk.peek() <= stack.peek():
                    stack.push(stk.peek())
                    stk.pop()
        # move the elements back
        while not stack.isEmpty():
            stk.push(stack.peek())
            stack.pop()
