"""
Implement a function to check if a linked list is a palindrome.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# reverse the second half
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        from math import ceil
        if not head or not head.next:
            return True
        length, cur = 0, head
        while cur:
            length, cur = length + 1, cur.next
        cur = head
        for i in range(int(ceil(length / 2))):
            cur = cur.next
        reverse_half = self.reverseList(cur)
        cur = head
        while reverse_half:
            if cur.val != reverse_half.val:
                return False
            cur, reverse_half = cur.next, reverse_half.next
        return True
        
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

# reverse the first half 
class Solution2:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        reverse, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next
            
        tail = head.next if fast else head
        
        # Compare the reversed first half list with the second half list.
        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            if not is_palindrome:
                return False
            reverse, tail = reverse.next, tail.next
        return True
