"""
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?
Example
Given array S = [3,4,6,7], return 3. They are:

[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
"""

class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        if not S or len(S) == 0:
            return 0
        count = 0
        S.sort()
        for i in range(2, len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count
