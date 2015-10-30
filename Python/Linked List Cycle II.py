"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break
        if fast is None or fast.next is None:
            return None
        slow = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast
