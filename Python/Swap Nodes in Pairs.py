"""
Given a linked list, swap every two adjacent nodes and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next, cur, prev = head, head, dummy
        while cur and cur.next:
            next_node = cur.next.next
            prev.next = cur.next
            prev.next.next = cur
            cur.next = next_node
            cur = cur.next
            prev = prev.next.next
        return dummy.next
