"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution1:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        dummy = ListNode(-1)
        dummy.next, prev = head, dummy 
        while head:
            prev_value, is_duplicated = head.val, False
            while head.next and head.next.val == prev_value:
                head = head.next
                is_duplicated = True
            if not is_duplicated:
                prev.next = head
                prev = prev.next
            head = head.next
        # remove the tail
        prev.next = None
        return dummy.next

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution2:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head or not head.next:
            return head
        p = head.next
        if p.val == head.val:
            while p and p.val == head.val:
                head.next = p.next
                p = p.next
            return self.deleteDuplicates(p)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
