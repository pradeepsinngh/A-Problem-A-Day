'''
# Prob: Leftmost Column with at Least a One

'''


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows, cols = binaryMatrix.dimensions()
        res = float('inf')
        
        for r in range(rows):
            left, right = 0, cols
            while left < right:
                mid = left + (right-left) // 2
                currVal = binaryMatrix.get(r,mid)
                
                if currVal == 0:
                    left = mid + 1
                else:
                    right = mid
                
            if left < cols and binaryMatrix.get(r, left) == 1:
                res = min(res, left)
        
        if res < float('inf'):
            return res
        else:
            return -1
                
                
                
