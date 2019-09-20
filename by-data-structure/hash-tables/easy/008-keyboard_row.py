# Keyboard Row:
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard 
# like the image below.

# Example:

# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

# Sol1 :
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        list1 = set('qwertyuiop')
        list2 = set('asdfghjkl')
        list3 = set('zxcvbnm')
        
        res = []
        
        for word in words:
            w = set(word.lower())
            
            if w <= list1 or w <= list2 or w <= list3:
                res.append(word)
            
        return res
            
