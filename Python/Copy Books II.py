"""
Given n books( the page number of each book is the same) and an array of integer with size k means k people to copy the book and the i th integer is the time i th person to copy one book). 
You must distribute the continuous id books to one people to copy. (You can give book A[1],A[2] to one people, but you cannot give book A[1], A[3] to one people, because book A[1] and A[3] is not continuous.) 
Return the number of smallest minutes need to copy all the books.

Example
Given n = 4, array A = [3,2,4], .

Return 4( First person spends 3 minutes to copy book 1, Second person spends 4 minutes to copy book 2 and 3, Third person spends 4 minutes to copy book 4. )
"""

class Solution:
    # @param n: an integer
    # @param times: a list of integers
    # @return: an integer
    def copyBooksII(self, n, times):
        # write your code here
        if not times or n == 0:
            return 0
        k = len(times)
        """
        dp[i][j] is the minimum time to copy j books with i people
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(k)]
        for i in range(1, n + 1):
            dp[0][i] = i * times[0]
        for i in range(1, k):
            for j in range(1, n + 1):
                dp[i][j] = float('inf')
                for p in range(j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][j - p], p * times[i]))
                    if dp[i - 1][j - p] <= p * times[i]:
                        break
        return dp[-1][-1]
