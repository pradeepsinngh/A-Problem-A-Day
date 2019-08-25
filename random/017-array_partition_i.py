# Prob: Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), 
# (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        sum_so_far = 0
        
        for i in range(0, len(nums)-1,2):
            sum_so_far += nums[i]
        
        return sum_so_far
        
