"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

# O(n^2) time and O(n^2) space
class Solution1:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        max_length = 0
        result = ""
        lookup = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    if j - i + 1 > max_length:
                        max_length = max(max_length, j - i + 1)
                        result = s[i:j + 1]
        return result

# O(n^2) time O(1) space
class Solution2:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        if len(s) == 0:
            return 0
        result = s[0:1]
        
        for i in range(len(s)-1):
            p1 = self.expandAroundCenter(s, i, i)
            if len(p1) > len(result):
                result = p1
                
            p2 = self.expandAroundCenter(s, i, i+1)
            if len(p2) > len(result):
                result = p2
        return result
        
    def expandAroundCenter(self, s, c1, c2):
        l = c1
        r = c2
        M = len(s)
        while l >=0 and r < M and s[l] == s[r]:
            l -=1
            r +=1
            
        return s[l + 1:r]
