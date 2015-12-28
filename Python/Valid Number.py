"""
Validate if a given string is numeric.

Example
"0" => true

" 0.1 " => true

"abc" => false

"1 a" => false

"2e10" => true
"""

class Solution:
    # @param {string} s the string that represents a number
    # @return {boolean} whether the string is a valid number
    def isNumber(self, s):
        # Write your code here
        s = s.strip()
        i = 0
        while i < len(s) and s[i] != 'e':
            i += 1
        if i == 0 or i == len(s) - 1:
            return False

        def helper(s, has_dot):
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if not s or s == '.':
                return False
            for i in range(len(s)):
                if s[i] == '.':
                    if has_dot:
                        return False
                    has_dot = True
                elif ord('0') > ord(s[i]) or ord(s[i]) > ord('9'):
                    return False
            return True
        if i == len(s):
            return helper(s, False)
        return helper(s[:i], False) and helper(s[i + 1:], True)
