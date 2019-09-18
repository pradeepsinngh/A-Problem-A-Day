# Prob: Matrix Cells in Distance Order
# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

# Additionally, we are given a cell in that matrix with coordinates (r0, c0).

# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to 
# largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        listCord, disCord = [], []
        
        for r in range(R):
            for c in range(C):
                disCord += [abs(r - r0) + abs(c - c0)]
                listCord += [[r,c]]
                
        dis, cord = zip(*sorted(zip(disCord, listCord)))
        return cord
