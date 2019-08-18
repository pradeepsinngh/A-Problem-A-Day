# Prob: Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array. Example:

# Input: [1,3,5,6], 5
# Output: 2

class Solution(object):
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        
        for num in nums:
            if num >= target:
                return nums.index(num)
        return len(nums)
