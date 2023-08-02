
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        n=len(prices)
        maxprofit = 0
        minprice = sys.maxsize
        for i in range(n):
            minprice = min(minprice,prices[i])
            maxprofit = max(maxprofit,prices[i]-minprice)
        return maxprofit
    
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
