```
Prob: Contiguous Array
- Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

```

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        max_len = 0
        
        dic = {0:0}
        
        for index, num in enumerate(nums,1):
            if num == 0:
                count -= 1
            else:
                count += 1
                
            if count in dic:
                max_len = max(max_len, index - dic[count])
            else:
                dic[count] = index
        return max_len
