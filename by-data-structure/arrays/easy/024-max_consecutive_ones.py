```
Max Consecutive Ones:
Given a binary array, find the maximum number of consecutive 1s in this array.

```
# Sol1 :

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        counter = 0
        for num in nums:
            
            if num == 1:
                counter += 1
                if counter > max_ones:
                    max_ones = counter
            else:
                counter = 0
            
        return max_ones
