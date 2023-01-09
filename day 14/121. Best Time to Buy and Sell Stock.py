
# Solution Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/874664528/

class Solution:
    def maxProfit(self, prices) -> int:
        maxprice = 0
        n = len(prices)
        minprice  = prices[0]
        for i in range(n):
            minprice = min(minprice,prices[i])
            maxprice = max(maxprice,prices[i] - minprice)

        return maxprice