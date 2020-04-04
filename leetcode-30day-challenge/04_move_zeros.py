```
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

```

Sol 1: Using two for loops
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        for j in range(n-1):
            for i in range(n-1):
                if nums[i] == 0:
                    nums[i+1], nums[i] = nums[i], nums[i+1]

