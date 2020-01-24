# Problem: 
# Design Stack with MAx API

# Time: O(1)
# Space: O(n)


class StackWithMax(object):

	def __init__(self):
		self.Stack = []
		self.trackStack = []

	def pop(self, x):
		self.Stack.pop()

	def push(self, x):

		self.Stack.append(x)

		if (len(self.Stack) == 1):
			self.trackStack.append(x)
			return

		if x > self.trackStack[-1]:
			self.trackStack.append(x)
		else:
			self.trackStack.append(self.trackStack[-1])

	def getMax(self):
		return self.trackStack[-1]

# Driver Code 
if __name__ == '__main__': 
  
    s = StackWithMax() 
    s.push(20)  
    print(s.getMax())  
    s.push(10)  
    print(s.getMax()) 
    s.push(50)  
    print(s.getMax())
