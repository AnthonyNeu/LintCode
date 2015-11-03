"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.



For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

Example
given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

Note
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates or len(candidates) == 0:
            return []
        candidates.sort()
        n = len(candidates)
        
        def dfs(current, idx, x):
            if x == 0:
                result.append(list(current))
            else:
                i = idx
                while i < n:
                    if x < candidates[i]:
                        break
                    dfs(current + [candidates[i]], i, x - candidates[i])
                    i += 1
        result = []
        dfs([], 0, target)
        return result
