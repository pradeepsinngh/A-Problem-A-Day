```
Prob: Last Stone Weight

We have a collection of stones, each stone has a positive integer weight. Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

```

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
                
        
