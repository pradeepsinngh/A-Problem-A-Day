'''
# Prob: First Unique Number
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

- FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
- int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
- void add(int value) insert value to the queue.

'''

class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dict = collections.Counter(nums)
        self.q = collections.deque()
        
        for i in nums:
            if self.dict[i] == 1:
                self.q.append(i)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        return self.q[0] if len(self.q) else -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.dict[value] = self.dict.get(value, 0) + 1
        
        if self.dict[value] == 1:
            self.q.append(value)
       
        while self.q and self.dict[self.q[0]]>1:
            self.q.popleft()
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
