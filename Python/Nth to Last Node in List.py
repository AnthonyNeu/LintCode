"""
Find the nth to last element of a singly linked list. 

The minimum number of nodes in list is n.
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
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        length, cur = 0, head
        while cur:
            cur, length = cur.next, length + 1
        for i in range(length - n):
            head = head.next
        return head
