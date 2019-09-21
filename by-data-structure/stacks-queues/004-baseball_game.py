# Prob: Baseball game



# Sol1: Using stack

Time Complx: O(N)
Space Complx: O(N)

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        res = []
        
        for op in ops:
            if op == '+':
                res.append(res[-1] + res[-2])
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == 'C':
                res.pop()
            else:
                res.append(int(op))
                
        return sum(res)
                
                
