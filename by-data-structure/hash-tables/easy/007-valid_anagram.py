# Prob: Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.


# Sol1: 

class Solution(object):
    def isAnagram(self, s, t):
        seen = {}
        
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
                
        for j in t:
            if j not in seen:
                return False
            else:
                seen[j] -= 1
                
        for val in seen.values():
            if val != 0:
                return False
        
        return True
        
  
# Sol2 :

class Solution(object):
    def isAnagram(self, s, t):
        
        return sorted(s) == sorted(t)
