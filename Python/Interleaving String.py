"""
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
"""

class Solution1:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if len(s1) + len(s2) != len(s3):
            return False
        match = [[False for i in xrange(len(s2) + 1)] for j in xrange(len(s1) + 1)]
        match[0][0] = True
        for i in xrange(1, len(s1) + 1):
            match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in xrange(1, len(s1) + 1):
            for j in xrange(1, len(s2) + 1):
                match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return match[-1][-1]

# Time:  O(m * n)
# Space: O(m + n)
# Dynamic Programming + Sliding Window
class Solution2:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):
            return self.isInterleave(s2, s1, s3)
        match = [False for i in xrange(len(s1) + 1)]
        match[0] = True
        for i in xrange(1, len(s1) + 1):
            match[i] = match[i -1] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0] = match[0] and s2[j - 1] == s3[j - 1]
            for i in xrange(1, len(s1) + 1):
                match[i] = (match[i - 1] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i] and s2[j - 1] == s3[i + j - 1])
        return match[-1]
