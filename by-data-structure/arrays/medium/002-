```
Prob: Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

```

# Sol1: Traverse through array, make a hast table, counting how many time each number is occuring, return 
# numbers whioch occured twice

Time Complx: O(n)
Space Complx: O(n)

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        dic = collections.Counter(nums)
        res = []
        
        for v, k in dic.items():
            if k == 2:
                res.append(v)
                
        return res


# Sol2: Do linear pass through list, make every number -ve if you see 


Time Complx: O(n)
Space Complx: O(1)
