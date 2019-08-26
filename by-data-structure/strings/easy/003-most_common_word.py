# Prob: Most Common Word

# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.


# Sol1:

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        banset = set(banned)
        
        for c in "!?,;.'":
            paragraph = paragraph.replace(c, " ")
        
        count = collections.Counter(word for word in paragraph.lower().split())
        
        ans, best = '', 0
        
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]
                
        return ans
                
                
        
