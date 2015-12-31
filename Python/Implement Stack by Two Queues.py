"""
Implement a stack by two queues. The queue is first in first out (FIFO). 
That means you can not directly pop the last element in a queue.
"""

class Stack:
    # initialize your data structure here.
    def __init__(self):
        from collections import deque
        self.q1, self.q2 = deque([]), deque([])

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        """
        pop all the elements in q1 then add them back to the end of q1.
        """
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        return self.q1.popleft()

    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        return self.q1[0]

    # @return an boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return len(self.q1) == 0
