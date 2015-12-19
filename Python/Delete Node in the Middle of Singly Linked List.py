"""
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

Example
Given 1->2->3->4, and node 3. return 1->2->4
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        prev, cur = None, node
        while cur.next:
            prev = cur
            cur.val = cur.next.val
            cur = cur.next
        prev.next = None
