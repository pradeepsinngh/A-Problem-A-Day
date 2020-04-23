'''
# Prob: Min Cost Climbing Stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.


Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        cost.append(0)
        dp = [0] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(n+1):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return dp[n]
