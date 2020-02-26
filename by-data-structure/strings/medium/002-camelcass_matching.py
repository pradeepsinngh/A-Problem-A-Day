# Prob: Camelcase Matching -- https://leetcode.com/problems/camelcase-matching/
```
A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.
```
class Solution:
    def camelMatch(self, queries, pattern):
        
        res = []
        for query in queries:
            res.append(self.patt_match(query, pattern))
        return res
    

    def patt_match(self, query, pattern):
        j = 0
        for char in query:
            if j < len(pattern) and char == pattern[j]:
                j += 1
            elif ord('Z') >= ord(char) >= ord('A'):
                return False
        print(j)   
        return len(pattern) == j
