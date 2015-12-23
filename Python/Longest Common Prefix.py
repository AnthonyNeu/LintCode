"""
Given k strings, find the longest common prefix (LCP).

Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"

For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"
"""

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ""
        flag, idx = True, 0
        while True:
            if len(strs[0]) <= idx:
                break
            c = strs[0][idx]
            for i in range(1, len(strs)):
                if len(strs[i]) <= idx or strs[i][idx] != c:
                    flag = False
                    break
            if not flag:
                break
            idx += 1
        return strs[0][:idx]
