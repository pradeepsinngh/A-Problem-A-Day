# Design Hash Map
# -----------------

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [ [ [],[] ] for i in range(self.size) ]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket, idx = self._index(key)

        
        if idx == -1:
            bucket[0].append(key)
            bucket[1].append(value)
        else:
            bucket[0][idx] = key
            bucket[1][idx] = value


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, idx = self._index(key)
        if idx == -1: return -1
        return bucket[1][idx]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket, idx = self._index(key)
        if idx == -1:
            pass
        else:
            bucket[0].pop(idx)
            bucket[1].pop(idx)

    def _hash(self, key):
        return key % self.size
    
    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for idx, k in enumerate(bucket[0]):
            if k == key:
                return bucket, idx
        return bucket, -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
