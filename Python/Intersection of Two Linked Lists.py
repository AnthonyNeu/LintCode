"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Note
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Challenge
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        """
        the idea is if you switch head, the possible difference between length would be countered.
        On the second traversal, they either hit or miss.
        if they meet, pa or pb would be the node we are looking for,
        if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
        """
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 and p2 and p1 is not p2:
            p1, p2 = p1.next, p2.next
            if p1 is p2:
                return p1
            if not p1:
                p1 = headB
            if not p2:
                p2 = headA
        return p1
