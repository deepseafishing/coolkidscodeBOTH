class Chain:

    def __init__(self):
        self.chain = []

    def get(self, key):
        for (k, v) in self.chain:
            if (k == key):
                return v
        return -1

    def update(self, key, value):
        for idx, k in enumerate(self.chain):
            if (k[0] == key):
                self.chain[idx] = (key, value)
                return
        self.chain.append((key, value))

    def remove(self, key):
        for idx, k in enumerate(self.chain):
            if(key == k[0]):
                del self.chain[idx]


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 2000
        self.map = [Chain() for i in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_result = key % self.capacity
        self.map[hash_result].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.map[key % self.capacity].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.map[key % self.capacity].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
