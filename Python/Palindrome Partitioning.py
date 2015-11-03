"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
"""

class Solution1:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        N = len(s)
        lookup = [[False for _ in xrange(N)] for _ in xrange(N)]
        for i in reversed(range(N)):
            for j in range(i, N):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
        
        def dfs(current, idx):
            if idx == N:
                result.append(list(current))
            else:
                for i in range(idx, N):
                    if lookup[idx][i]:
                        dfs(current + [s[idx:i + 1]], i + 1)
        result = []
        dfs([], 0)
        return result

class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        n = len(s)
        is_palindrome = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2 ) or is_palindrome[i + 1][j - 1])
        sub_partition = [[] for i in xrange(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[j + 1]:
                            sub_partition[i].append([s[i:j + 1]] + p)
                    else:
                        sub_partition[i].append([s[i:j + 1]])
        return sub_partition[0]
