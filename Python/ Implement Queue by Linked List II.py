"""
Implement a Queue by linked list. Provide the following basic methods:

push_front(item). Add a new item to the front of queue.
push_back(item). Add a new item to the back of the queue.
pop_front(). Move the first item out of the queue, return it.
pop_back(). Move the last item out of the queue, return it.

Example
push_front(1)
push_back(2)
pop_back() // return 2
pop_back() // return 1
push_back(3)
push_back(4)
pop_front() // return 3
pop_front() // return 4
"""

class Dequeue(object):

    def __init__(self):
        # do some intialize if necessary
        self.head, self.tail = None, None

    # @param {int} item an integer
    # @return nothing
    def push_front(self, item):
        # Write yout code here
        if not self.head:
            self.head = ListNode(item)
        else:
            node = ListNode(item)
            node.next = self.head
            if not self.tail:
                self.tail = self.head
            self.head = node

    # @param {int} item an integer
    # @return nothing
    def push_back(self, item):
        # Write yout code here
        if not self.head:
            self.head = ListNode(item)
        else:
            if self.tail:
                self.tail.next = ListNode(item)
                self.tail = self.tail.next
            else:
                self.head.next = ListNode(item)
                self.tail = self.head.next

    # @return an integer
    def pop_front(self):
        # Write your code here
        val = self.head.val
        self.head = self.head.next
        # only one node left, we need to set self.tail to None
        if self.head and not self.head.next:
            self.tail = None
        return val

    # @return an integer
    def pop_back(self):
        # Write your code here
        prev, cur = None, self.head
        while cur and cur.next:
            prev = cur
            cur = cur.next
        val = cur.val
        # no node left
        if not prev:
            self.head = None
        # one node left
        elif prev == self.head:
            self.tail = None
            self.head.next = None
        # more than one node left
        else:
            self.tail = prev
            self.tail.next = None
        return val
