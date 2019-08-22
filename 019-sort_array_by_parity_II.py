# Prob: Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.


# -------------
# Sol 1: Two Pass

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        N = len(A)
        sortedArr = [None] * N
        
        i = 0
        for num in A:
            if num % 2 == 0:
                sortedArr[i] = num
                i += 2
                
        i = 1
        for num in A:
            if num % 2 == 1:
                sortedArr[i] = num
                i += 2
        
        return sortedArr
                
  Time Complx.: O(N)
  Space Complx: O(1)
           
           
# -------------
# Sol 2: 
