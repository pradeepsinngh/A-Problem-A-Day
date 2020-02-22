# Prob: We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        heap = []
        
        for x, y in points:
            dist = -(x*x + y*y)
            
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x ,y))
            else:
                heapq.heappush(heap, (dist,x,y))
                
        return [[x,y] for dist, x, y in heap]
