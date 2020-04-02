```
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true

Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

```

## Sol 1:

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        if n < 1:
            return False
        
        seen = set()
        
        nums = n
        totalSum = 0
        
        while n not in seen:
            seen.add(n)
            nums = self.getNum(n)
            totalSum = self.getSum(nums)
            if totalSum == 1:
                return True
            n = totalSum
    
    def getSum(self, nums):
        totalSum = 0
        for num in nums:
            totalSum = totalSum + (num * num)
        return totalSum
    
    def getNum(self, n):
        nums = []
        while n>9:
            temp = n % 10
            nums.append(temp)
            n = n / 10
        nums.append(n)
        return nums
        
            
## ---------------------            
## Sol 2: Convert number into string and iterator over each char.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen = set()
        
        while n not in seen:
            seen.add(n)
            strN = str(n)
            
            totalSum = 0
            for char in strN:
                totalSum += int(char) * int(char)
            
            if totalSum == 1:
                return True
            
            n = totalSum
            








