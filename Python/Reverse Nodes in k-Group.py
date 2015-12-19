"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

Example
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        cur, count = head, 0
        while cur and count < k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                temp = head.next
                head.next = cur
                cur = head
                head = temp
                count -= 1
            head = cur
        return head

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        if k <= 1 or not head:
            return head
        reverse_times = self.length(head) / k
        dummy = ListNode(-1)
        dummy.next, prev, cur = head, dummy, head
        while reverse_times > 0:
            for i in range(k - 1):
                next_node = cur.next
                cur.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node 
            prev = cur
            cur = cur.next
            reverse_times -= 1
        return dummy.next
        
    def length(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count
