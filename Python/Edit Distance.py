"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        dp = [[i] for i in range(len(word1) + 1)]
        dp[0] = [j for j in range(len(word2) + 1)]
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                insert = dp[i][j - 1] + 1
                delete = dp[i - 1][j] + 1
                replace = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                dp[i].append(min(insert, delete, replace))
        return dp[len(word1)][len(word2)]
