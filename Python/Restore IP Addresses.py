"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Given "25525511135", return

[
  "255.255.11.135",
  "255.255.111.35"
]
Order does not matter.
"""

class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        # Write your code here
        result = []

        def helper(cur, idx, num):
            if idx == len(s) and num == 4:
                result.append(cur)
                return
            # last one is more than 3 digits
            if len(s) - idx > 3 * (4 - num):
                return
            # all the remaining digits is not enough
            if len(s) - idx < 4 - num:
                return
            for i in range(idx, min(len(s), idx + 3)):
                candidate = s[idx:i + 1]
                if (i - idx > 0 and s[idx] == '0') or int(candidate) > 255:
                    continue
                helper(cur + candidate if num == 0 else cur + '.' + candidate, i + 1, num + 1)
        helper("", 0, 0)
        return result

class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        # Write your code here
        M = len(s)
        result = []
        for i in range(1,min(4, M - 2)):
            for j in range(i + 1, min(i + 4, M - 1)):
                for k in range(j + 1,min(j + 4, M)):
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                    if self.isValid(s1) and self.isValid(s2) and self.isValid(s3) and self.isValid(s4):
                        result.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
        return result

    def isValid(self,s):
        if len(s) > 3 or len(s) == 0 or (s[0] == '0' and len(s) > 1) or int(s) > 255:
            return False
        return True
