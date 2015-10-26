"""
Design an algorithm and write code to serialize and deserialize a binary tree. 
Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, you only need to make sure you can serialize a binary tree to a string and deserialize this string to the original structure.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# use level-order traversal
class Solution1:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        
        def levelOrder():
            queue = []
            if root is None:
                return []
            result, is_last = [], False
            queue.append(root)
            while len(queue) > 0 and not is_last:
                is_last, n, visit = True, len(queue), []
                while n > 0:
                    n -= 1
                    node = queue.pop(0)
                    if not node:
                        visit.append('#')
                        queue += [None, None]
                    else:
                        visit.append(str(node.val))
                        is_last = False
                        queue += [node.left, node.right]
                result += visit
            return result
        return levelOrder()
    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if data is None or len(data) == 0:
            return None
        root = TreeNode(int(data[0]))
        parents, idx = [root], 1
        while idx < len(data):
            next_parents = []
            while parents:
                node = parents.pop(0)
                if not node:
                    next_parents += [None, None]
                else:
                    node.left, node.right = [TreeNode(int(data[i])) if data[i] != '#' else None for i in range(idx, idx + 2)]
                    next_parents += [node.left, node.right]
                idx += 2
            parents = next_parents
        return root

# use Preorder traversal
class Solution2:


    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code herer
        self.res = ''
        
        def serialize_helper(root):
            if not root:
                self.res += '# '
                return 
            else:
                self.res += str(root.val) + ' '
                serialize_helper(root.left)
                serialize_helper(root.right)
        serialize_helper(root)
        return self.res

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        nodes = data.split(" ")
        nodes.pop()
        self.res = None
        self.pointer = 0
        
        def deserialize_helper():
            if nodes[self.pointer] != '#':
                new_node = TreeNode(int(nodes[self.pointer]))
                if not self.res:
                    self.res = new_node
                self.pointer += 1
                new_node.left = deserialize_helper()
                new_node.right = deserialize_helper()
                return new_node
            else:
                self.pointer += 1
                return None
        deserialize_helper()
        return self.res