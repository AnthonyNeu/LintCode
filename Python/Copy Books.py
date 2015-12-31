"""
Given an array A of integer with size of n( means n books and number of pages of each book) and k people to copy the book.
You must distribute the continuous id books to one people to copy.
(You can give book A[1],A[2] to one people, but you cannot give book A[1], A[3] to one people, because book A[1] and A[3] is not continuous.) Each person have can copy one page per minute.
Return the number of smallest minutes need to copy all the books.

Example
Given array A = [3,2,4], k = 2.

Return 5( First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )
"""

# binary search, n * log (p), p is the sum of the pages
class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        """
        use binary search, try to find the lowest pages each person can copy.
        """
        length = len(pages)
        if k >= length:
            return max(pages)
        total_sum = sum(pages)

        # check whether everyone can copy at most x pages or not
        def valid(x):
            cur_sum, people, idx = 0, 0, 0
            while idx < length and people < k:
                if cur_sum + pages[idx] > x:
                    cur_sum = 0
                    people += 1
                cur_sum += pages[idx]
                idx += 1
            return people < k and cur_sum <= x

        def binary_search(left, right):
            while left + 1 < right:
                mid = left + (right - left) / 2
                if valid(mid):
                    right = mid
                else:
                    left = mid
            return left if valid(left) else right
        return binary_search(total_sum / k, total_sum)

# O(n^2 * k) DP solution
# when we add new people, we need to check whether it will reduce time for him to copy books p to j
class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        length = len(pages)
        sum_from_start = [0 for _ in range(length)]
        for i in range(length):
            sum_from_start[i] = sum_from_start[i - 1] + pages[i]
        dp = [[float('inf') for _ in range(length)] for _ in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(length):
                if i == 1 or j == 0:
                    dp[i][j] = sum_from_start[j]
                else:
                    for p in range(j - 1, -1, -1):
                        cur = max(dp[i - 1][p], sum_from_start[j] - sum_from_start[p])
                        dp[i][j] = min(cur, dp[i][j])
        return dp[k][length - 1]

# Do speed up by two pointers, O(n * k) time
class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        length = len(pages)
        k = min(length, k)
        sum_from_start = [0 for _ in range(length)]
        for i in range(length):
            sum_from_start[i] = sum_from_start[i - 1] + pages[i]
        dp = [[float('inf') for _ in range(length)] for _ in range(k + 1)]
        dp[1][:] = sum_from_start[:]
        for i in range(2, k + 1):
            dp[i][0] = sum_from_start[0]
            left, right = 0, 1
            while right < length:
                current = sum_from_start[right] - sum_from_start[left]
                dp[i][right] = min(max(dp[i - 1][left], current), dp[i][right])
                """
                As dp[i - 1][j] is increasing as j increases:
                Move left if dp[i - 1][left] > sum(left + 1, right), or left == right.
                Move right otherwise. Also move left back by 1 step in this case, since it would be a potential solution.
                """
                if left < right and dp[i - 1][left] < current:
                    left += 1
                else:
                    right += 1
                    if left > 0:
                        left -= 1
        return dp[k][length - 1]
