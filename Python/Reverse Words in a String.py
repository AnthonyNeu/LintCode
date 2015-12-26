"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        result, word = "", ""
        for c in s:
            if c != ' ':
                word += c
            elif len(word) > 0:
                if result != '':
                    result = ' ' + result
                result = word + result
                word = ''
        if len(word) > 0:
            if result != '':
                    result = ' ' + result
            result = word + result
        return result
