# Prob: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        currSum = nums[0]
        maxSum = currSum
                
        for x in range(1,len(nums)):
            if currSum < nums[x] and currSum < 0:
                currSum = nums[x]
            else:
                currSum += nums[x]
                
            maxSum = max(currSum, maxSum)
        
        return maxSum
