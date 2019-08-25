# Prob: Relative Sort Array

# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
# Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        finalArr = []
        N = len(arr1)
        
        for num in arr2:
            counter = 0
            for i in range(N):
                
                if num == arr1[i]:
                    finalArr.append(num)
        
        op = []
        for i in range(N):
            if arr1[i] not in arr2:
                op.append(arr1[i])
                
        finalArr = finalArr + sorted(op)
        
        return finalArr
                    
