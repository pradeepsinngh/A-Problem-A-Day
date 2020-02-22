# Prob: Implement int sqrt(int x).

class Solution(object):
    
    def mySqrt(self, x):
        # newton method
        num = x
        while num * num > x:
            num = (num + x / num )/2
        
        return num
        
       # Binary search  
    #    l, r = 0, x
    #    while l <= r:
    #        mid = l + (r-l)//2
    #        if mid * mid <= x < (mid+1)*(mid+1):
    #            return mid
    #        elif x < mid * mid:
    #            r = mid
    #        else:
    #            l = mid + 1
                
    
