# Prob: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        current = 0
        next = 1
        length = len(nums)
        
        while next < length:
            
            currNum = nums[current]
            nextNum = nums[next]
            
            if currNum != nextNum:
                current += 1
                print(current)
                nums[current] = nums[next]
            next += 1
            
        return current+1
            
            
