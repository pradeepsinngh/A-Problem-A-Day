'''
# Prob:  Best Time to Buy and Sell Stock I 

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        T_i10 = 0
        T_i11 = float('-inf')
        
        for price in prices:
            T_i10 = max(T_i10, T_i11 + price)
            T_i11 = max(T_i11, -price)
        return T_i10


## -----------------------------------
## -----------------------------------

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_so_far, profit = float('Inf'), 0
        for price in prices:
            min_so_far = min(price, min_so_far)
            profit = max(profit, price - min_so_far)

        return profit
