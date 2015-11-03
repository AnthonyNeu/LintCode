"""
Given n unique integers, number k (1<=k<=n)  and target. Find all possible k integers where their sum is target.
"""
class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # write your code here
        if not A or len(A) == 0:
            return []
        result = []
        A.sort()
        
        def dfs(target, k, current, idx):
            if target == 0 and k == 0:
                result.append(list(current))
            elif target == 0 or k == 0:
                return
            else:
                i = idx
                while i < len(A):
                    if A[i] > target:
                        break
                    dfs(target - A[i], k - 1, current + [A[i]], i + 1)
                    i += 1
        dfs(target, k, [], 0)
        return result
