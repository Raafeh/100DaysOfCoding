class MyHashMap:

    def __init__(self):
        self.size = 1000  # Choose a suitable size for the array of buckets.
        self.buckets = [None] * self.size

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = []
        
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key: int) -> int:
        index = self.hash(key)
        if not self.buckets[index]:
            return -1
        
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        if not self.buckets[index]:
            return
        
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Test:

myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))  # Output: 1
print(myHashMap.get(3))  # Output: -1
myHashMap.put(2, 1)
print(myHashMap.get(2))  # Output: 1
myHashMap.remove(2)
print(myHashMap.get(2))  # Output: -1
