"""
Remove all elements from a linked list of integers that have value val.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        dummy = TreeNode(0)
        prev, dummy.next  = dummy, head
        while head:
            if head.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
