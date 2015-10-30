"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
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
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return head
        dummy, bigger = ListNode(-1), ListNode(-1)
        dummy.next = head
        p1, p2 = dummy, bigger
        while head:
            if head.val >= x:
                p2.next = head
                p2 = p2.next
            else:
                p1.next = head
                p1 = p1.next
            head = head.next
        p2.next = None
        p1.next = bigger.next
        return dummy.next
