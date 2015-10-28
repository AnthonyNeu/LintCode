"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""

class Solution1: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        ways = [[0 for _ in xrange(len(T) + 1)] for _ in range(len(S) + 1)]
        for i in range(len(S) + 1):
            ways[i][0] = 1
        for i, S_char in list(enumerate(S)):
            for j, T_char in reversed(list(enumerate(T))):
                if S_char == T_char:
                    ways[i + 1][j + 1] = ways[i][j] + ways[i][j + 1]
                else:
                    ways[i + 1][j + 1] = ways[i][j + 1]
        return ways[-1][-1]

class Solution2:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [0 for _ in xrange(len(T) + 1)]
        ways[0] = 1
        for S_char in S:
            for j, T_char in reversed(list(enumerate(T))):
                if S_char == T_char:
                    ways[j + 1] += ways[j]
        return ways[len(T)]
        