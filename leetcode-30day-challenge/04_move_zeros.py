```
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

```

# Sol 1: Using two for loops
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


                    
# Sol 2: Two pointer approach
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Input: [0,1,0,3,12]
        i = 0
        j = 0
        while(i < len(nums)):
            if nums[j] != 0:
                j += 1
            else:
                if nums[i] != 0:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            i += 1
            
