```
Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.

```
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def build(s):
            res = []
            for c in s:
                if c != '#':
                    res.append(c)
                elif res:
                    res.pop()
            return ''.join(res)
        
        return build(S) == build(T)
