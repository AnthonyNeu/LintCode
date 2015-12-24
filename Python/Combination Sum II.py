"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Example
For example, given candidate set 10,1,6,7,2,1,5 and target 8,

A solution set is:

[1,7]

[1,2,5]

[2,6]

[1,1,6]

Note
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
"""

class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        result = []
        candidates.sort()
        def helper(current, target, start):
            if target == 0:
                result.append(current)
            else:
                n, i = len(candidates), start
                while i < n:
                    if candidates[i] <= target:
                        helper(current + [candidates[i]], target - candidates[i], i + 1)
                        i += 1
                        while i < n and candidates[i] == candidates[i - 1]:
                            i += 1
                    else:
                        break
        helper([], target, 0)
        return result
