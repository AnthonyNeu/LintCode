"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example
Given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        """
        'left', represents how many left parentheses remains;
        'right' represents how many right parentheses remains.
        The remaining right parentheses should be larger than left ones.
        """
        result = []

        def helper(cur, left, right):
            if left == right == 0:
                result.append(cur)
            if left > 0:
                helper(cur + '(', left - 1, right)
            if left < right:
                helper(cur + ')', left, right - 1)
        helper("", n, n)
        return result

# A more easy backtracking solution
class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        result = []

        def helper(cur, left, right):
            if left == right == 0:
                result.append(cur)
            if left > right or left < 0 or right < 0:
                return
            helper(cur + '(', left - 1, right)
            helper(cur + ')', left, right - 1)
        helper("", n, n)
        return result

# DP solution
# https://leetcode.com/discuss/11509/an-iterative-method
class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        """
        First consider how to get the result f(n) from previous result f(0)...f(n-1).
        Actually, the result f(n) will be put an extra () pair to f(n-1).
        Let the "(" always at the first position, to produce a valid result, we can only put ")" in a way that there will be i pairs () inside the extra () and n - 1 - i pairs () outside the extra pair.

        Let us consider an example to get clear view:

        f(0): ""

        f(1): "("f(0)")"

        f(2): "("f(0)")"f(1), "("f(1)")"

        f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"

        So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"
        """
        lists = [[""]]
        for i in range(1, n + 1):
            f = []
            for j in range(i):
                for m in lists[j]:
                    for n in lists[i - 1 - j]:
                        f.append('(' + m + ')' + n)
            lists.append(f)
        return lists[-1]

# https://leetcode.com/discuss/43122/4-7-lines-python
class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))
