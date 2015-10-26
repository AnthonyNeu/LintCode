"""
Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        """
        Notice: the reason we set min_cut[len(s)] = -1 is to simplify the code below
        if lookup[i][len(s) - 1] is True, then we need 0 cut to let s[i:] to be a palindrome
        So min_cut[len(s)] + 1 = 0.
        """ 
        min_cut = [len(s) - i - 1 for i in range(len(s) + 1)]
        lookup = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    min_cut[i] = min(min_cut[i], min_cut[j + 1] + 1)
        return min_cut[0]
