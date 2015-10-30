"""
You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in forward order, such that the 1's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists2(self, l1, l2):
        # Write your code here
        result = self.addLists(self.reverseList(l1), self.reverseList(l2))
        return self.reverseList(result)
        
    def reverseList(self, head):
        if head is None:
            return head
        new_head, cur = None, head
        while cur:
            temp = cur.next
            cur.next = new_head
            new_head = cur
            cur = temp
        return new_head
    
    def addLists(self, l1, l2):
        dummy, carry = ListNode(0), 0
        current = dummy
        while l1 or l2:
            if l1 and l2:
                result = l1.val + l2.val + carry
            else:
                tail = l1 or l2
                result = tail.val + carry
            carry = result / 10
            current.next = ListNode(result % 10)
            current= current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # for carry > 0
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next
