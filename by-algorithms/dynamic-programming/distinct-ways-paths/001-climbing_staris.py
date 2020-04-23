'''
# Prob: Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        ans = [1,2] + [0] * (n-2)
        for i in range(2,n):
            ans[i] = ans[i-1]+ ans[i-2]
        return ans[n-1]


