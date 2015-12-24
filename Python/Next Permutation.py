"""
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]

Note
The list may contains duplicate integers.
"""

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        """
        https://leetcode.com/discuss/38247/algorithm-wikipedia-implementation-permutations-permutations
        1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, the permutation is sorted in descending order, just reverse it to ascending order and we are done. For example, the next permutation of [3, 2, 1] is [1, 2, 3].
        2. Find the largest index l greater than k such that nums[k] < nums[l].
        3. Swap the value of nums[k] with that of nums[l].
        4. Reverse the sequence from nums[k + 1] up to and including the final element nums[nums.size() - 1].
        """
        k, l = -1, 0
        for i in xrange(len(num) - 1):
            if num[i] < num[i + 1]:
                k = i
        if k == -1:
            num.reverse()
        else:
            for i in range(k + 1, len(num)):
                if num[i] > num[k]:
                    l = i
            num[k], num[l] = num[l], num[k]
            num[k + 1:] = num[:k:-1]
        return num
