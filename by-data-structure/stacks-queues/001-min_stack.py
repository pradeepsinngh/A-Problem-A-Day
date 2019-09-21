# Prob: Min Stack:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Sol:

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x,x))

    def pop(self):
        if len(self.stack): 
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None
        
        
  
