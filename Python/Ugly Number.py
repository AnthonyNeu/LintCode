"""
Ugly number is a number that only have factors 3, 5 and 7.

Design an algorithm to find the Kth ugly number. The first 5 ugly numbers are 3, 5, 7, 9, 15 ...

"""

class Solution1:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        # write your code here
        i3, i5, i7 = 0, 0, 0
        ugly = [1]
        while len(ugly) <= k:
            while 3 * ugly[i3] <= ugly[-1]: i3 += 1
            while 5 * ugly[i5] <= ugly[-1]: i5 += 1
            while 7 * ugly[i7] <= ugly[-1]: i7 += 1
            ugly.append(min(ugly[i3] * 3, ugly[i5] * 5, ugly[i7] * 7))
        return ugly[-1]

class Solution2:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        # write your code hereugly_number = 0
        import heapq
        heap = []
        heapq.heappush(heap, 1)
        for _ in range(k + 1):
            ugly_number = heapq.heappop(heap)
            if ugly_number % 3 == 0:
                heapq.heappush(heap, ugly_number * 3)
            elif ugly_number % 5 == 0:
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)
            else:
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)
                heapq.heappush(heap, ugly_number * 7)
        return ugly_number
