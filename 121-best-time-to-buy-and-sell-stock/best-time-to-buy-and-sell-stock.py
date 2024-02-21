class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            diff = max(diff, price - lowest)
        return diff