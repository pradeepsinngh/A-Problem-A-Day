# Prob: Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}

        for index, num in enumerate(numbers):
            other = target - num
            
            if other in seen:
                return [seen[other]+1, index+1]
            else:
                seen[num] = index
                
        return []
