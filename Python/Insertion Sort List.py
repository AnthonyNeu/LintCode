"""
Sort a linked list using insertion sort.
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution1:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next, cur = head, head
        while cur:
            while cur.next and cur.val <= cur.next.val:
                cur = cur.next
            # insert cur.next
            if cur.next and cur.val > cur.next.val:
                insert, cur.next, prev = cur.next, cur.next.next, dummy
                while prev.next:
                    if insert.val > prev.next.val:
                        prev = prev.next
                    else:
                        insert.next, prev.next = prev.next, insert
                        break
            else:
                cur = cur.next
        return dummy.next
    
class Solution2:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0)
        while head:
            node = dummy
            # find the insertion position
            while node.next and node.next.val < head.val:
                node = node.next
            temp = head.next
            head.next = node.next
            node.next = head
            head = temp
        return dummy.next
