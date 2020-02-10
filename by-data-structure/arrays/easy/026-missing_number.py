# Problem: Missing number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Sol 1: Hastset
        
        #num_set = set(nums)
        #n = len(nums) + 1
        #for i in range(n):
        #    if i not in nums:
        #        return i
            
        # Sol 2: Gauss Formula
        
        expected_sum = len(nums) * (len(nums) + 1)//2
        actual_sum = sum(nums)
        
        missing_num = expected_sum - actual_sum
        return missing_num
