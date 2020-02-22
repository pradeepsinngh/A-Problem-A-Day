# Prob: Last Stone Weight

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1 and heap[0] != 0:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            heapq.heappush(heap, stone1 - stone2)
            
        return -heap[0]
