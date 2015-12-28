"""
Given an absolute path for a file (Unix-style), simplify it.

Example
"/home/", => "/home"

"/a/./b/../../c/", => "/c"

Challenge
Did you consider the case where path = "/../"?

In this case, you should return "/".

Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".

In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        # Write your code here
        tokens, stack = path.split('/'), []
        for token in tokens:
            if token == '..' and stack:
                stack.pop()
            if token != '..' and token != '.' and token:
                stack.append(token)
        return '/' + '/'.join(stack)
