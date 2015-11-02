"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

# use double linkedlist and hash table 
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache1:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        
    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.dic:
            return -1
        cur = self.dic[key]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.move_to_tail(cur)
        return cur.value
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        # Notice: we need to move this node when it is updated
        if self.get(key) != -1:
            self.dic[key].value = value
            return
        if len(self.dic) == self.capacity:
            del self.dic[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        new_node = Node(key, value)
        self.dic[key] = new_node
        self.move_to_tail(new_node)
        
    # @param cur, a Node
    # @return nothing
    def move_to_tail(self, cur):
        cur.prev = self.tail.prev
        self.tail.prev = cur
        cur.prev.next = cur
        cur.next = self.tail

class LRUCache2:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        
    # @return an integer
    def get(self, key):
        # write your code here
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key not in self.cache and len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        elif key in self.cache:
            del self.cache[key]
        self.cache[key] = value

