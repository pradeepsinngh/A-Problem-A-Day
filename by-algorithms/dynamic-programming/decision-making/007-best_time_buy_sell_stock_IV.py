'''
# Prob: Best Time to Buy and Sell Stock IV

Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
'''

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        if k >= len(prices) and len(prices) > 1:
            T_ik0 = 0
            T_ik1 = float('-inf')
    
            for price in prices:
                T_ik0_old = T_ik0
                T_ik0 = max(T_ik0, T_ik1 + price)
                T_ik1 = max(T_ik1, T_ik0_old - price)
        
            return T_ik0;
        
        T_ik0 = [0] * (k+1)
        T_ik1 = [float('-inf')] * (k + 1)
        print(T_ik0)
        print(T_ik1)

        
        for price in prices:
            for j in range(k,0,-1):
                T_ik0[j] = max(T_ik0[j], T_ik1[j] + price)
                T_ik1[j] = max(T_ik1[j], T_ik0[j - 1] - price)
        
        return T_ik0[k]
