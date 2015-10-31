"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
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
        profit, min_price = 0, float('inf')
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            profit = max(profit, prices[i] - min_price)
        return profit
