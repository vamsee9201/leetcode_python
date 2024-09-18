class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = 0
        sell = 1
        maxProfit = -100000
        highestSellIndex = len(prices) - 1
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if currentProfit >= maxProfit:
                maxProfit = currentProfit
                highestSellIndex = sell
            sell = sell+1
        while buy < highestSellIndex:
            currentProfit = prices[highestSellIndex] - prices[buy]
            if currentProfit > maxProfit:
                maxProfit = currentProfit
            buy = buy + 1
        if maxProfit > 0:
            return maxProfit
        else:
            return 0

            



        
        