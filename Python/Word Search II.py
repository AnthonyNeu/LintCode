"""
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. 
A word can start from any position in the matrix and go left/right/up/down to the adjacent position. 
"""

class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.children = {}
        
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_leaf = True 

class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        from sets import Set
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if not board or len(board) == 0 or len(board[0]) == 0:
            return []
        if not words or len(words) == 0:
            return []
        m, n = len(board), len(board[0])
        result, visited = Set(), [[False for _ in range(n)] for _ in range(m)]
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        def dfs(i, j, node, current):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
                return
            if board[i][j] not in node.children:
                return
            current.append(board[i][j])
            next_trie_node = node.children[board[i][j]]
            if next_trie_node.is_leaf:
                result.add(''.join(current))
            visited[i][j] = True
            for direction in directions:
                dfs(i + direction[0], j + direction[1], next_trie_node, current)
            visited[i][j] = False
            current.pop()
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, [])
        return list(result)
