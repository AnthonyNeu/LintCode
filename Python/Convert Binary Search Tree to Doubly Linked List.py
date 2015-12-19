"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    head, tail = None, None
    def bstToDoublyList(self, root):
        # Write your code here
        def convert(root):
            if not root:
                return
            convert(root.left)
            if self.head is None:
                self.head = DoublyListNode(root.val)
                self.tail = self.head
            else:
                node = DoublyListNode(root.val)
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            convert(root.right)
        convert(root)
        return self.head

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        if not root:
            return None
        head, tail, stack = None, None, []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            if head is None:
                head = DoublyListNode(node.val)
                tail = head
            else:
                new_node = DoublyListNode(node.val)
                new_node.prev = tail
                tail.next = new_node
                tail = new_node
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return head
