"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution1:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        
        # combine the copied list and the original list
        current = head
        while current:
            copy = RandomListNode(current.label)
            copy.next = current.next
            current.next = copy
            current = copy.next
        
        # update the random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
            
        # split the result from the original list
        current = head
        dummy = RandomListNode(0)
        prev = dummy
        while current:
            prev.next = current.next
            current.next = current.next.next
            prev = prev.next
            current = current.next
        return dummy.next

class Solution2:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        dummy = RandomListNode(0)
        prev, current, table = dummy,head,{}
        while current:
            copy = RandomListNode(current.label)
            table[current] = copy
            prev.next = copy
            prev, current = prev.next, current.next
        current = head
        while current:
            if current.random:
                table[current].random = table[current.random]
            current = current.next
        return dummy.next
