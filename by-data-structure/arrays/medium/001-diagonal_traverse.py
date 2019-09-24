```
Prob: Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
```

# Sol1: 
Time Complx: O(m + n), where m + n is total number of elt in matrix
Space Complx: O(m + n)

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = []
        dic = collections.defaultdict(list)
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dic[i+j+1].append(matrix[i][j])
                
        for key in dic.keys():
            if key % 2 == 1:
                dic[key].reverse()
            
            res += dic[key]
            
        return res
