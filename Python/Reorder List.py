"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.
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
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head:
            return None
        a, b = self.splitList(head)
        b = self.reverseList(b)
        head = self.mergeLists(a, b)
        
    def splitList(self, head):
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        return head, middle
        
    def reverseList(self, head):
        if head is None:
            return head
        new_head, cur = None, head
        while cur:
            temp = cur.next
            cur.next = new_head
            new_head = cur
            cur = temp
        return new_head
        
    def mergeLists(self, a, b):
        head, tail = a, a
        while b:
            # store the next node of tail and b
            b_next = b.next
            a_next = tail.next
            # append b to the end of tail
            tail.next = b
            b.next = a_next
            # move the tail and b
            tail = tail.next.next
            b = b_next
        return head
