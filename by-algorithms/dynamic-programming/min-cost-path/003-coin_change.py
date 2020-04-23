'''
# Prob : Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount +1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
