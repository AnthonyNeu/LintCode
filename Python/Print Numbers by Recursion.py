"""
Print numbers from 1 to the largest number with N digits by recursion.

Example
Given N = 1, return [1,2,3,4,5,6,7,8,9].

Given N = 2, return [1,2,3,4,5,6,7,8,9,10,11,12,...,99].

Note
It's pretty easy to do recursion like:

recursion(i) {
    if i > largest number:
        return
    results.add(i)
    recursion(i + 1)
}
however this cost a lot of recursion memory as the recursion depth maybe very large. 
Can you do it in another way to recursive with at most N depth?

Challenge
Do it in recursion, not for-loop.
"""

class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        # write your code here
        result = []

        def helper(cur):
            if cur == n:
                return
            if cur == 0:
                result.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                size = len(result)
                for i in range(1, 10):
                    high_digit = i * (10 ** cur)
                    result.append(high_digit)
                    for j in range(size):
                        result.append(result[j] + high_digit)
            helper(cur + 1)
        helper(0)
        return result
