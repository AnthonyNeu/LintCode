"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        from collections import deque
        queue = deque([start])
        length = 1
        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                if word == end:
                    return length
                N = len(word)
                for j in range(N):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:j] + char + word[j + 1:]
                        if candidate in dict:
                            queue.append(candidate)
                            dict.remove(candidate)
            length += 1
        return 0
