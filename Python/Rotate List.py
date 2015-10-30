"""
Given a list, rotate the list to the right by k places, where k is non-negative.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if not head or not head.next:
            return head
        cur, length = head, 1
        while cur.next:
            cur, length = cur.next, length + 1
        cur.next = head
        k = k % length
        for i in range(length - k):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
