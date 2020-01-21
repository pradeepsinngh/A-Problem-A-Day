# Problem: Duplicate Zeros
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Sol 1:

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        l = len(arr)
        while i < l:
            if arr[i]==0:
                arr.insert(i,0)
                arr.pop()
                i += 1
            i +=1
            
        return arr
