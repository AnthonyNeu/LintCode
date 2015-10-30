"""
Write code to remove duplicates from an unsorted linked list.
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def removeDuplicates(self, head):
        # Write your code here
        from sets import Set
        dummy, table = ListNode(0), Set()
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val not in table:
                table.add(current.next.val)
                current = current.next
            else:
                current.next = current.next.next
        return dummy.next
