# Prob: Given an array nums and a value val, remove all instances of that value in-place and return the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
            
        return i
                
