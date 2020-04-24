'''
# Prob: Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        T_i10 = 0
        T_i11 = float('-inf')
        T_i20 = 0
        T_i21 = float('-inf')
        
        for price in prices:
            T_i20 = max(T_i20, T_i21 + price)
            T_i21 = max(T_i21, T_i10 - price)
            T_i10 = max(T_i10, T_i11 + price)
            T_i11 = max(T_i11, -price)
        
        return T_i20
        
