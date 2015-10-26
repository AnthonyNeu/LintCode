"""
Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.
"""

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            return len(s) == 0
            
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        
        max_length = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, max_length) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break
        return f[n]
