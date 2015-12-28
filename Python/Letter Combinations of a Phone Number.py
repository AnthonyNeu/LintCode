"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Example
Given "23"

Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Note
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        # Write your code here
        if not digits:
            return []
        lookup, res = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
        def helper(current, length):
            if length == len(digits):
                res.append(current)
                return
            for choice in lookup[int(digits[length])]:
                helper(current + choice, length + 1)
        helper("", 0)
        return res

# iterative solution
class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        # Write your code here
        if not digits:
            return []
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], [""]
        for i in range(len(digits)):
            idx = ord(digits[i]) - ord('0')
            next_level = []
            for j in range(len(lookup[idx])):
                for k in range(len(result)):
                    next_level.append(result[k] + lookup[idx][j])
            result = next_level
        return result
