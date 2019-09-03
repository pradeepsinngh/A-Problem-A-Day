# Prob: Jewels and Stones
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Sol1: 
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        dic = {}
        
        for letter in J:
            dic[letter] = 0
            
        for letter in S:
            if letter in dic:
                dic[letter] += 1
                
        return sum(dic.values())
            
            
