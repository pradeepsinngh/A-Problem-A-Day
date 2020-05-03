'''
# Prob: Perform String Shift

You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

- direction can be 0 (for left shift) or 1 (for right shift). 
- amount is the amount by which string s is to be shifted.
- A left shift by 1 means remove the first character of s and append it to the end.
- Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
- Return the final string after all operations.

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

'''



class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """

        netShift = 0
        for sh in shift:
            if sh[0] == 0:
                netShift -= sh[1]
            else:
                netShift += sh[1]
        
        return s[-netShift::] + s[0:-netShift]
     
        
        
