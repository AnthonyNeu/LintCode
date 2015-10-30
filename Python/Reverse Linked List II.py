"""
Reverse a linked list from position m to n.
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
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(0)
        dummy.next, prev = head, dummy
        for i in range(1, n + 1):
            if i < m :
                prev = prev.next
            elif i == m:
                # the last node which is swapped
                last = prev.next
                cur = last.next
            else:
                # Notice, this reverse method is not the same as reorder list
                # As we already have the previous node of the reversed list
                # we only need to keep track of the current node and the last of the reversed list
                last.next = cur.next
                cur.next = prev.next
                prev.next = cur
                cur = last.next
        return dummy.next
