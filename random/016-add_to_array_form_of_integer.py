# Prob: Add to Array-Form of Integer

# For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].
# Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.


# ---------------------
# Sol 1:

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        A[-1] += K
        for i in range(len(A)-1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        
        return A
            

# ------------------
# Sol 2:

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        
        if len(A) > 1:
            num = 0
            for i in range(len(A)):
                num += A[i] * pow(10, len(A)-1-i)
        else:
            num = A[0]
            
        num = num + K
        output = [str(i) for i in str(num)]
        
        return output
