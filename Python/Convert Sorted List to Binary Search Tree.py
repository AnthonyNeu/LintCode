"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if head is None:
            return None
        cur, length, self.head = head, 0, head
        while cur:
            cur, length = cur.next, length + 1
        
        def sortedListToBSTHelper(left, right):
            if left > right:
                return None
            mid = left + (right - left) / 2
            left_root = sortedListToBSTHelper(left, mid - 1)
            root = TreeNode(self.head.val)
            root.left, self.head = left_root, self.head.next
            right_root = sortedListToBSTHelper(mid + 1, right)
            root.right = right_root
            return root
        root = sortedListToBSTHelper(0, length - 1)    
        return root
