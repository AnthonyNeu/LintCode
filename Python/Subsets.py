"""
Given a set of distinct integers, return all possible subsets.
"""

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        if S is None or not S:
            return []
        result = []
        length = len(S)
        total = 2 ** length - 1
        S.sort()
        while total >= 0:
            cur, idx, subset = total, 0, []
            while idx < length:
                if cur & 1:
                    subset.append(S[idx])
                idx += 1
                cur >>= 1
            result.append(subset)
            total -= 1
        return result

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        if S is None or not S:
            return []
        result = []
        S.sort()

        def subsetsHelper(idx, current):
            if idx == len(S):
                result.append(current)
            else:
                subsetsHelper(idx + 1, current)
                subsetsHelper(idx + 1, current + [S[idx]])
        subsetsHelper(0, [])
        return result
        