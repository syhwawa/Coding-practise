"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


1. Define and iterate min price of the list
2. iterate max_pro
"""

# Solution 1：

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0 ,float('Inf')
        
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price-min_price)
            
        return max_profit
        
  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
         if len(prices) <= 1:
            return 0
        
        price = prices[0]
        maxp = 0
        
        for i in range(1, len(prices)):
            price = min(price, prices[i])
            maxp = max(maxp, prices[i] - price)
        return maxp

