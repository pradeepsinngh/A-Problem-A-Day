# Prob: Occurrences After Bigram

Given words first and second, consider occurrences in some text of the form "first second third", where second comes 
immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 
Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

# Sol1: 

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
        split_txt = text.split()
        len_text = len(split_txt)
        print(len_text)
        ans = []
        
        for i in range(0,len_text-2):
            if split_txt[i] == first:
                if split_txt[i+1] == second:
                    ans.append(split_txt[i+2])
                
        return ans
