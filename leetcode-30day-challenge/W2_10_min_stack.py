class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x,x))
        self.size += 1
        
        

    def pop(self):
        """
        :rtype: None
        """
        if self.size:
            self.stack.pop()
            self.size -= 1
        

    def top(self):
        """
        :rtype: int
        """
        if self.size:
            return self.stack[-1][0]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.size:
            return self.stack[-1][1]
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
