# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = next

class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.head = None
        self.tail = None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
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
    def dequeue(self):
        # Write your code here
        val = self.head.val
        self.head = self.head.next
        return val
