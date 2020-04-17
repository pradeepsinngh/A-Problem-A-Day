'''
# Prob: Valid Parenthesis String
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. 

We define the validity of a string by these rules:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
- An empty string is also valid.
'''

# Sol1 : Using two stacks

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        star = []
        
        for i, st in enumerate(s):
            if st == '(':
                stack.append(i)
            elif st == '*':
                star.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while stack and star:
            if stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                break    
        
        return len(stack) == 0
        
        
  # Sol 2: 

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = right = 0
        
        for st in s:
            if st == '(':
                left += 1
            else:
                left -= 1
            
            if st != ')':
                right += 1
            else:
                right -= 1
                
            if right < 0:
                break
            left = max(left, 0)
        return left == 0
                
