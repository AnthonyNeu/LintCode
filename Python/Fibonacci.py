"""
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Example
Given 1, return 0

Given 2, return 1

Given 10, return 34

Note
The Nth fibonacci number won't exceed the max value of signed 32-bit integer in the test cases.
"""


class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        dp = [0 for _ in range(n + 1)]
        dp[1] = 0
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

# O(n) time and O(1) space
class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        prev, cur = 0, 1
        for i in range(n - 2):
            prev, cur = cur, prev + cur
        return cur

# O(log n) time and O(1) space
# http://www.gocalf.com/blog/calc-fibonacci.html
class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        mat = [[1, 1], [1, 0]]
        mat = self.MatrixPower(mat, n - 2)
        return mat[0][0]

    def MatrixMultiply(self, x, y):
        # x is a m*a matrix, y is a a*n matrix.
        # x * y is a m*n matrix.
        m = len(x)
        n = len(y[0])
        a = len(x[0])
        # transpose y
        y = [[y[i][j] for i in xrange(a)] for j in xrange(n)]
        res = [[self.DotProduct(x[j], y[i]) for i in xrange(n)] for j in xrange(m)]
        return res

    def MatrixPower(self, mat, n):
        res = None
        temp = mat
        while True:
            if n & 1:
                if res is None:
                    res = temp
                else:
                    res = self.MatrixMultiply(res, temp)
            n >>= 1
            if n == 0:
                break
            temp = self.MatrixMultiply(temp, temp)
        return res

    def DotProduct(self, x, y):
        """
        vector x, y must have the same length.
        """
        n = len(x)
        s = 0
        for i in xrange(n):
            s += x[i] * y[i]
        return s
