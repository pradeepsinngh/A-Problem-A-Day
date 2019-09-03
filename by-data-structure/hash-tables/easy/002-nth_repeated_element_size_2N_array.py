# Prob: N-Repeated Element in Size 2N Array
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

# Return the element repeated N times.

# Sol1 : Count -  Hashmaps

 Time Complx = O(n)
 Sapce Complx = O(N)

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        count = collections.Counter(A)
        
        for k in count:
            if count[k] > 1:
                return k
                
              
