"""
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.
"""

class Queue:

    def __init__(self):
        # use to hold the newly inserted element
        self.stack1 = []
        # use as a queue
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
        return self.stack2[-1]

    def pop(self):
        # write your code here
        # pop and return the top element
        element = self.top()
        self.stack2.pop()
        return element
