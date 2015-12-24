"""
Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

Example
For [1,3,2,3], the previous permutation is [1,2,3,3]

For [1,2,3,4], the previous permutation is [4,3,2,1]

Note
The list may contains duplicate integers.
"""

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, num):
        # write your code here
        k, l = -1, 0
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                k = i
        if k == -1:
            num.reverse()
        else:
            for i in range(k + 1, len(num)):
                if num[i] < num[k]:
                    l = i
            num[k], num[l] = num[l], num[k]
            num[k + 1:] = num[:k:-1]
        return num
