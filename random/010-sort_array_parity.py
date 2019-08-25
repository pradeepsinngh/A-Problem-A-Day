# Prob: Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
# followed by all the odd elements of A.


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        evenList = []
        oddList = []
        opList = []
        
        for num in A:
            if num % 2 == 0:
                evenList.append(num)
            else:
                oddList.append(num)
        
        opList = evenList + oddList
        return opList
