"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Example
Given prices = [4,4,6,1,1,4,2,5], and k = 2, return 6.

Note
You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Challenge
O(nk) time.
"""

class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        if k >= len(prices) / 2:
            return self.maxAtMostNPairsProfit(prices)
        return self.maxAtMostKPairsProfit(prices, k)

    def maxAtMostNPairsProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])     
        return profit

    def maxAtMostKPairsProfit(self, prices, k):
        # max_buy[j] means the most profit we can make using j-1 transactions and
        # for a specific stock prices[1:i-1],and buying stock at prices[i].
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        # max_sell[j] means the most profit we can make using j-1 transactions
        # and for a specific stock prices[1:i-1],and selling stock at prices[i].
        max_sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i / 2 + 1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i]) 
        return max_sell[k]
