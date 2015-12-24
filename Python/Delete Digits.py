"""
Given string A representative a positive integer which has N digits, remove any k digits of the number, the remaining digits are arranged according to the original order to become a new positive integer.

Find the smallest integer after remove k digits.

N <= 240 and k <= N,

Example
Given an integer A = "178542", k = 4

return a string "12"
"""

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        """
        O(nk) solution, each time remove the last number in the increasing sequence.
        """
        if len(A) == k:
            return ""
        for i in range(k):
            j = 0
            while j < len(A):
                if j == len(A) - 1 or A[j] > A[j + 1]:
                    A = A[:j] + A[j + 1:]
                    break
                j += 1
        i = 0
        while i < len(A) - 1 and A[i] == '0':
            i += 1
        return A[i:]

# Another solution use a stack. O(2n) time at the worst case.
class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        stack, count, result = [], 0, ""
        for i in range(len(A)):
            num = A[i]
            if not stack or num >= stack[-1]:
                stack.append(num)
            else:
                if count == k:
                    stack.append(num)
                else:
                    # we can move digit now
                    while count < k and stack and stack[-1] > num:
                        stack.pop()
                        count += 1
                    stack.append(num)
        while count < k:
            stack.pop()
            count += 1
        result = "".join(stack)
        i = 0
        while i < len(result) - 1 and result[i] == '0':
            i += 1
        return result[i:]
