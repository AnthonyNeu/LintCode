"""
Merge two sorted (ascending) linked lists and return it as a new sorted list. 
The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
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
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2=l2.next
                head = head.next
            else:
                head.next = l1
                l1=l1.next
                head = head.next
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        else:
            head.next = None
        return dummy.next
