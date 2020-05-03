'''
Prob: Product of Array Except Self:

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Input:  [1,2,3,4]
Output: [24,12,8,6]
'''

# Sol 1: Left and Right product lists

# T - O(N)
# Space - O(N)

class Solution:
    def productExceptSelf(self, nums):
        
        n = len(nums)
        L, R, answer = [0]*n, [0]*n, [0]*n

        L[0] = 1
        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]

        R[n-1] = 1
        for i in reversed(range(n - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        
        for i in range(n):
            answer[i] = L[i] * R[i]
        
        return answer
        
        
 # Sol 2:
 # T - O(N)
 # S - O(1)
 
 class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * n
        
        answer[0] = 1
        for i in range(1,n):
            answer[i] = answer[i-1] * nums[i-1]
        
        R = 1
        for i in reversed(range(n)):
            answer[i] = answer[i] * R
            R = R * nums[i]
            
        return answer
