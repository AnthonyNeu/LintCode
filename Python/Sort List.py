"""
Sort a linked list in O(n log n) time using constant space complexity.
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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        l1, l2 = self.splitList(head)
        sorted_l1 = self.sortList(l1)
        sorted_l2 = self.sortList(l2)
        return self.mergeTwoLists(sorted_l1, sorted_l2)
        
    # in this split, we need to let the later one has at last 1 node
    # not the same splitList as the reorder list
    def splitList(self, head):
        if not head:
            return None
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        return head, slow
        
    def mergeTwoLists(self, l1, l2):
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
        