"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Challenge
O(n3) time
"""

# 3-way DP, O(n ^ 3)
class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        if len(s1) != len(s2):
            return False
        length = len(s1)    
        dp = [[[False for _ in range(length)] for _ in range(length)] for _ in range(length + 1)]
        for i in range(length):
            for j in range(length):
                dp[1][i][j] = s1[i] == s2[j]
        for l in range(1, length + 1):
            for i in range(length - l + 1):
                for j in range(length - l + 1):
                    if l == 1:
                        dp[1][i][j] = s1[i] == s2[j]
                    elif dp[l][i][j] is False:
                        for p in range(1, l):
                            if (dp[p][i][j] and dp[l - p][i + p][j + p]) or (dp[p][i][j + l - p] and dp[l - p][i + p][j]):
                                dp[l][i][j] = True
        return dp[length][0][0]

# recursion
class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) < 4 or s1 == s2:
            return True
        return self.isScrambleRe(s1, s2);
            
    def isScrambleRe(self, s1, s2):
        if sorted(s1) != sorted(s2):
            return False
        if len(s1) == 0 or len(s1) == 1:
            return True
        for i in xrange(1, len(s1)):
            if self.isScrambleRe(s1[:i], s2[:i]) and self.isScrambleRe(s1[i:], s2[i:]) or \
            self.isScrambleRe(s1[:i], s2[-i:]) and self.isScrambleRe(s1[i:], s2[:-i]):
                return True
        return False

# recursion using memorization      
class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) < 4 or s1 == s2:
            return True
        self. m = {}
        return self.isScrambleRe(s1, s2);
            
    def isScrambleRe(self, s1, s2):
        if sorted(s1) != sorted(s2):
            return False
        if len(s1) == 0 or len(s1) == 1:
            return True
        if (s1, s2) in self.m:
            return self.m[(s1, s2)]
        for i in xrange(1, len(s1)):
            if self.isScrambleRe(s1[:i], s2[:i]) and self.isScrambleRe(s1[i:], s2[i:]) or \
            self.isScrambleRe(s1[:i], s2[-i:]) and self.isScrambleRe(s1[i:], s2[:-i]):
                self.m[(s1, s2)] = True
                return True
        return False
