"""
Count the number of k's between 0 and n. k can be 0 - 9.
"""

# Brute-force method
class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        from collections import Counter
        result = 0
        for i in range(n + 1):
            counter = Counter(str(i))
            result += counter[str(k)]
        return result

# http://www.hawstein.com/posts/20.4.html
class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        count, factor = 0, 1
        while n / factor != 0:
            low = n - (n / factor) * factor
            cur = (n / factor) % 10
            high = n / (factor * 10)
            if cur < k:
                count += high * factor
            elif cur == k:
                count += high * factor + low + 1
            elif cur > k:
                # when k == 0 and we are calculating the highest digit, we cannot set this digit to 0
                # as these numbers are already included
                count += high * factor if k == 0 and n / factor < 10 else (high + 1) * factor
            factor *= 10
        return count
