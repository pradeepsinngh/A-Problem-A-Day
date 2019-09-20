# Prob: Largest Perimeter Triangle
# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of 
# these lengths.
# If it is impossible to form any triangle of non-zero area, return 0.



# Sol1 : Sort the array and check for largest pair such that a + b > c
Time Complx: O(n)
Space Compx: O(n)

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        A.sort()
        largestp = 0
        perimeter = 0
        
        for i in range(len(A)-2):
            if A[i] + A[i+1] > A[i+2]:
                perimeter = A[i] + A[i+1] + A[i+2]
                if perimeter > largestp:
                    largestp = perimeter
        
        return largestp
            
            
 # sol2 : Credits: Leetcode -- Once array is sorted, you can traves through array from back and check for a + b >c
 
 class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        A.sort()
        largestp = 0
        perimeter = 0
        
        for i in range(len(A)-3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                largestp = A[i] + A[i+1] + A[i+2]
                return largestp
        
        return 0
