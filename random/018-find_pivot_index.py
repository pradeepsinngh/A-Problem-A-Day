# Prob: Find Pivot Index

# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sumLeft = 0
        totalSum = sum(nums)
        
        for i, x in enumerate(nums):
            sumRight = totalSum - sumLeft - x
            if sumLeft == sumRight:
                return i
            sumLeft += x
            
        return -1
