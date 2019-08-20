# Prob: Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ncols = len(A[0])
        
        temp = []
        op = []
        
        for i in range(ncols):
            for x in A:
                temp.append(x[i])
            op.append(temp)
            temp = []
        return op
        
        
