"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next, cur = head, head
        while cur and cur.next and cur.next.val == cur.val:
            cur = cur.next
        dummy.next = cur
        if cur.next:
            cur.next = self.deleteDuplicates(cur.next)
        return dummy.next
