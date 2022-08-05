class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                break
            if prices[i+1] - prices[i] > 0:
                profit += (prices[i+1] - prices[i])
        return profit
        