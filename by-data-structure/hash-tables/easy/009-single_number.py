# Prob: Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Sol1: Make a dic and check which key has value 1.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ndic = collections.Counter(nums)
        
        for key in ndic.keys():
            if ndic[key] == 1:
                return key
        
