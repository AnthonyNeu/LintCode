"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.
"""

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 0:
            return 0
        length = len(prices)
        left, right = [0 for _ in range(length)], [0 for _ in range(length)]
        # from left to right, left[i] is the max profit to sell at i
        min_price = prices[0]
        for i in range(1, length):
            min_price = min(prices[i], min_price)
            left[i] = max(left[i - 1], prices[i] - min_price)
        # for right to left, right[i] is the max profit to buy at i
        max_price = prices[-1]
        for i in reversed(range(length - 1)):
            max_price = max(prices[i], max_price)
            right[i] = max(right[i + 1], max_price - prices[i])
        return max(map(sum, zip(left, right)))
