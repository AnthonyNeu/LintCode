"""
Given a list of words and an integer k, return the top k frequent words in the list.

Example
Given

[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
for k = 3, return ["code", "lint", "baby"].

for k = 4, return ["code", "lint", "baby", "yes"],

Note
You should order the words by the frequency of them in the return list, the most frequent one comes first. 
If two words has the same frequency, the one with lower alphabetical order come first.
"""

# O(nlogk) time and O(n) extra space
class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        import heapq
        from collections import defaultdict
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        heap = []
        for key, value in dic.iteritems():
            heapq.heappush(heap, (-value, key))
        result = []
        while heap and k > 0:
            word = heapq.heappop(heap)
            result.append(word[1])
            k -= 1
        return result

# using for streaming
# from http://www.geeksforgeeks.org/find-the-k-most-frequent-words-from-a-file/
# O(nN+Nlogk) time, N is the intersection in the tire and O(k) space for the min heap.
from collections import defaultdict
class TrieNode:
    def __init__(self):
        # the end of word
        self.is_end = False
        # the number of occurences of a word
        self.freq = 0
        # the index of the word in minHeap
        self.index = -1
        # dic for children
        self.children = defaultdict(TrieNode)

class MinHeapNode:
    def __init__(self, root, freq, word):
        # the leaf node of the trie
        self.root = root
        # number of occurrences
        self.freq = freq
        # the actual word
        self.word = word

class MinHeap:
    def __init__(self):
        # the capacity
        self.capacity = 0
        # number of entry in the heap
        self.count = 0
        # list of min heap nodes
        self.node = []

class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        if k <= 0:
            return []
        min_heap = self._create_min_heap(k)
        root = TrieNode()
        for word in words:
            self.insert_word(root, min_heap, 0, word)
        result = []
        for i in range(min_heap.count):
            result.append(min_heap.node[0].word)
            min_heap.node[0], min_heap.node[min_heap.count - 1] = min_heap.node[min_heap.count - 1], min_heap.node[0]
            min_heap.count -= 1
            self._build_min_heap(min_heap)
        return result[::-1]

    def _create_min_heap(self, capacity):
        min_heap = MinHeap()
        min_heap.capacity = capacity
        return min_heap

    def _min_heapify(self, min_heap, idx):
        """
        this is the function to heapify the min heap.
        And it also updates the min index in the trie when
        two nodes are swapped in the min heap.
        """
        left, right = 2 * idx + 1, 2 * idx + 2
        smallest = idx
        if left < min_heap.count:
            if min_heap.node[left].freq < min_heap.node[smallest].freq or (min_heap.node[left].freq == min_heap.node[smallest].freq and min_heap.node[left].word > min_heap.node[smallest].word):
                smallest = left
        if right < min_heap.count:
            if min_heap.node[right].freq < min_heap.node[smallest].freq or (min_heap.node[right].freq == min_heap.node[smallest].freq and min_heap.node[right].word > min_heap.node[smallest].word):
                smallest = right
        if smallest != idx:
            # Update the corresponding index in Trie node.
            min_heap.node[smallest].root.index = idx
            min_heap.node[idx].root.index = smallest
            # swap node in min heap.
            min_heap.node[smallest], min_heap.node[idx] = min_heap.node[idx], min_heap.node[smallest]
            self._min_heapify(min_heap, smallest)

    def _build_min_heap(self, min_heap):
        """
        build a heap.
        """
        n = min_heap.count - 1
        for i in range((n - 1) / 2, -1, -1):
            self._min_heapify(min_heap, i)

    def _insert_to_min_heap(self, min_heap, root, word):
        # case 1: the word already in the min heap
        if root.index != -1:
            min_heap.node[root.index].freq += 1
            self._min_heapify(min_heap, root.index)
        # case 2: the word not in the min heap and the heap is not full
        elif min_heap.count < min_heap.capacity:
            min_heap.node.append(MinHeapNode(root, root.freq, word))
            root.index = min_heap.count
            min_heap.count += 1
            self._build_min_heap(min_heap)
        # case 3: the word not in the min heap and the heap is full
        # and the freq of the word is more than the min freq word in the heap
        # or the freq is the same but the alphabetical order is preferred.
        elif root.freq > min_heap.node[0].freq or (root.freq == min_heap.node[0].freq and word < min_heap.node[0].word):
            min_heap.node[0].root.index = -1
            min_heap.node[0] = MinHeapNode(root, root.freq, word)
            root.index = 0
            self._min_heapify(min_heap, 0)

    def insert_word(self, root, min_heap, current, word):
        if not root:
            root = TrieNode()
        if current != len(word):
            self.insert_word(root.children[word[current]], min_heap, current + 1, word)
        else:
            if root.is_end:
                root.freq += 1
            else:
                root.is_end = True
                root.freq = 1
            self._insert_to_min_heap(min_heap, root, word)

# bucket sort
class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        from collections import defaultdict
        table = defaultdict(int)
        max_count = 0
        for word in words:
            table[word] += 1
            max_count = max(max_count, table[word])
        count_array = [[] for i in range(max_count)]
        for word in table:
            count_array[table[word] - 1].append(word)
        res = []
        for j in range(max_count - 1, -1, -1):
            count_array[j].sort()
            for words in count_array[j]:
                if k == 0:
                    return res
                res.append(words)
                k -= 1
        return res
