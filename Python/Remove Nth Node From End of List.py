"""
Given a linked list, remove the nth node from the end of list and return its head.
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        length, cur = 0, head
        while cur:
            length, cur = length + 1, cur.next
        if length < n:
            return root
        dummy, idx = ListNode(float('inf')), 0
        prev, dummy.next = dummy, head
        while idx + n < length:
            prev = prev.next
            idx += 1
        prev.next = prev.next.next
        return dummy.next
