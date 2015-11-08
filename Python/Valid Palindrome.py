"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.
"""

class Solution1:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        i = 0
        j = len(s) -1 
        while i < j:
            while i < j and s[i].isalnum() is False:
                i += 1
            while i < j and s[j].isalnum() is False:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

class Solution2:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        from sets import Set
        alphabet = Set(list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        i = 0
        j = len(s) - 1
        gap = ord('a') - ord('A')
        while i < j:
            while i < j and s[i] not in alphabet:
                i += 1
            while i < j and s[j] not in alphabet:
                j -= 1
            if ord(s[i]) != ord(s[j]) and ord(s[i]) + gap != ord(s[j]) and \
                ord(s[i]) != ord(s[j]) + gap:
                return False
            i += 1
            j -= 1
        return True
