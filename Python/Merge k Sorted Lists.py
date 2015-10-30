"""
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return None
        while len(lists) > 1:
            new_lists = []
            for i in range(len(lists) / 2):
                new_lists.append(self.mergeTwoList(lists.pop(0), lists.pop()))
            if lists:
                new_lists.append(lists.pop())
            lists = new_lists
        return lists[0]
        
    def mergeTwoList(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
                head = head.next
            else:
                head.next = l1
                l1 = l1.next
                head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return dummy.next

class Solution2:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        import heapq
        # write your code here
        dummy, heap = ListNode(0), []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))
        current = dummy
        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next
