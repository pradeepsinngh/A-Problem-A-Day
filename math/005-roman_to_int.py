'''
# Prob: Roman to Integer
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {'I':1,'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        cuur = prev = sum = 0
        for i in s[::-1]:
            curr = dic[i]
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
        return sum


