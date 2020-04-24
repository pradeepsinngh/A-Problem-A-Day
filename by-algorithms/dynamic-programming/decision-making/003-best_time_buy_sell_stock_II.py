'''
# Prob: Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        T_ik0 = 0
        T_ik1 = float('-inf')
        
        for price in prices:
            T_ik0_old = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price)
            T_ik1 = max(T_ik1, T_ik0_old - price)
        return T_ik0

