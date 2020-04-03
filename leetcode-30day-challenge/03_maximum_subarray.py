```
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


```

# Sol1 : 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        currSum = nums[0]
        maxSum = currSum
        
        for i in range(1, len(nums)):
            if currSum < nums[i] and currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
                
            maxSum = max(currSum, maxSum)
        return maxSum
        
 # Sol 2 :
 
 
 
