class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}")
                return
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value {value}")

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key}")
                return
        print(f"Key {key} not found for deletion.")

    def display(self):
        print("Hash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

ht = HashTable()
ht.insert(15, "apple")
ht.insert(25, "banana")
ht.insert(35, "cherry")
print("Search 25:", ht.search(25))
ht.delete(25)
print("Search 25 after deletion:", ht.search(25))
ht.display()
