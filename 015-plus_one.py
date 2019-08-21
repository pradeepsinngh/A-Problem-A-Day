# Prob: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array 
# contain a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself.

# ----------
# Sol 1:

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits)-1-i)
            
        num = num + 1
        output = [str(i) for i in str(num)]
        
        return output 



# -----------
# Sol 2:

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        l = len(digits) - 1
        
        for i in range(l, -1, -1):
            if digits[i] > 8:
                digits[i] = 0
                #digits[i-1] = digits[i-1] + 1
            else:
                digits[i] = digits[i] + 1
                break
            
        return digits
