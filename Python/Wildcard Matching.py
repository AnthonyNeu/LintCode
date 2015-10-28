"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""

class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        if len(p) - p.count('*') > len(s):
            return False
        m, n = len(p), len(s)
        dp = [[False for j in range(m + 1)] for i in xrange(n + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]
