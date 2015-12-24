"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example
For example,
If n = 4 and k = 2, a solution is:
[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
"""

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        result = []
        def dfs(current, remain, start):
            if len(current) == k:
                result.append(current)
            else:
                for i in range(start, n + 2 - remain):
                    dfs(current + [i], remain - 1, i + 1)
        dfs([], k, 1)
        return result

# from https://leetcode.com/discuss/32955/a-short-recursive-java-solution-based-on-c-n-k-c-n-1-k-1-c-n-1-k
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if k == 0:
            return [[]]
        if k == n:
            return [[i for i in range(1, n + 1)]]
        result = self.combine(n - 1, k - 1)
        for l in result:
            l.append(n)
        result.extend(self.combine(n - 1, k))
        return result
