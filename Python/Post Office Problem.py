"""
On one line there are n houses.
Give you an array of integer means the the position of each house.
Now you need to pick k position to build k post office, so that the sum distance of each house to the nearest post office is the smallest.
Return the least possible sum of all distances between each village and its nearest post office.

Example
Given array a = [1,2,3,4,5], k = 2.
return 3.
"""

# Compute cost take O(n^3) time and O(n^2) space
# compute dp take O(kn^2) time and O(kn) space
class Solution:
    # @param {int[]} A an integer array
    # @param {int} k an integer
    # @return {int} an integer
    def postOffice(self, A, k):
        # Write your code here
        if not A:
            return 0
        n = len(A)
        if k >= n:
            return 0
        A.sort()
        cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        def compute_cost():
            """
            cost[i][j] is the minimum cost to build a office between house i and j
            This post office should be in the median of the houses.
            """
            for i in range(n):
                for j in range(i, n):
                    mid = i + (j - i) / 2
                    for r in range(i, mid + 1):
                        cost[i + 1][j + 1] += A[mid] - A[r]
                    for r in range(mid + 1, j + 1):
                        cost[i + 1][j + 1] += A[r] - A[mid]
        compute_cost()
        """
        dp[i][j] is the minimum cost for the first j houses with i post offices.
        """
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(k + 1)]
        dp[0][0] = 0
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                for r in range(j):
                    dp[i][j] = min(dp[i][j], dp[i - 1][r] + cost[r + 1][j])
        return dp[-1][-1]

# O(n^2) time solution
# http://blog.csdn.net/find_my_dream/article/details/4931222
class Solution:
    # @param {int[]} A an integer array
    # @param {int} k an integer
    # @return {int} an integer
    def postOffice(self, A, k):
        # Write your code here
        if not A:
            return 0
        n = len(A)
        if k >= n:
            return 0
        A.sort()
        """
        dp[i][j] is the minimum cost for the first j houses with i post offices.
        euclidean[i][j] is the euclidean distance between two houses.
        euclidean[i][j] = euclidean[i][j - 1] + abs(A[j - 1] - A[i - 1])
        s[i][j] is the position of last office we put to get dp[i][j].
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        euclidean = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                euclidean[i][j] = euclidean[i][j - 1] + abs(A[j - 1] - A[i - 1])

        def get_median(i, j):
            k = i + (j - i) / 2
            return euclidean[k][j] - euclidean[k][i - 1]
        for i in range(1, n + 1):
            dp[1][i] = get_median(1, i)
        for i in range(1, n + 1):
            """
            build a post office at each house.
            """
            s[i][i] = i
        for i in range(2, k + 1):
            j = n
            dp[i][j] = float('inf')
            """
            enumerate k from s[i - 1][j] to j - 1.
            As the following loops don't calculate the situation when j = n.
            """
            for k in range(s[i - 1][j], j):
                temp = dp[i - 1][k] + get_median(k + 1, j)
                if temp < dp[i][j]:
                    dp[i][j] = temp
                    s[i][j] = k
            for j in range(n - 1, i, -1):
                dp[i][j] = float('inf')
                """
                enumerate k from s[i - 1][j] to s[i][j + 1]
                """
                for k in range(s[i - 1][j], s[i][j + 1] + 1):
                    temp = dp[i - 1][k] + get_median(k + 1, j)
                    if temp < dp[i][j]:
                        dp[i][j] = temp
                        s[i][j] = k
        return dp[-1][-1]
