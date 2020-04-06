# Design Hash Set:

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket, idx= self._index(key)
        if idx >= 0:
            return
        bucket.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)
        
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket, idx = self._index(key)
        return idx >= 0
        
    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if key == k:
                return bucket, k
        return bucket, -1
        
    def _hash(self, key):
        return key % self.size


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
