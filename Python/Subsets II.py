"""
Given a list of numbers that may has duplicate numbers, return all possible subsets
"""

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        if S is None or not S:
            return []
        result = []
        S.sort()

        def subsetsHelper(idx, current):
            if idx == len(S):
                result.append(current)
            else:
                subsetsHelper(idx + 1, current + [S[idx]])
                i = idx + 1
                while i < len(S):
                    if S[idx] != S[i]:
                        break
                    i += 1
                subsetsHelper(i, current)
        subsetsHelper(0, [])
        return result
