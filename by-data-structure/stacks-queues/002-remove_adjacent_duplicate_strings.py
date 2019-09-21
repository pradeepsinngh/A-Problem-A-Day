# Prob: Remove All Adjacent Duplicates In String

# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# We repeatedly make duplicate removals on S until we no longer can.
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.


# Sol :

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        
        for letter in S:
            if res and letter == res[-1]:
                res.pop()
            else:
                res.append(letter)
                
        return ''.join(res)
                
            

