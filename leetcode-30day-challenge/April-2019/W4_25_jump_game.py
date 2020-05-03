'''
# PRob: Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        lastGoodIdx = n-1

        for i in range(len(nums))[::-1]:
            if (i+ nums[i]) >= lastGoodIdx:
                lastGoodIdx = i
        return not lastGoodIdx
        
            
