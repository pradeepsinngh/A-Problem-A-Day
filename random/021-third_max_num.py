# Prob: Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. 
# The time complexity must be in O(n).


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        uniqNum = []
        
        for num in nums:
            if num not in uniqNum:
                uniqNum.append(num)
            
        uniqNum = sorted(uniqNum)
        
        if len(uniqNum) < 3:
            return max(uniqNum)
        else:
            return uniqNum[-3]
