```
Prob: Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
```

# Sol1: 
Time Complx: O(N)
Sapce Complx: O(1)

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum_right = sum(nums)
        sum_left = 0
        
        for i in range(len(nums)):
            print(sum_left, sum_right)
            sum_right = sum_right - nums[i]
            
            if i != 0:
                sum_left = sum_left + nums[i-1]
            
            if sum_left == sum_right:
                return i
            
        return -1
