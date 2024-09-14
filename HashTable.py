class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key): #simple hash-function - mod from key divided by storage size
        return self.key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                self.table[index].remove(kvp)
                return True
        return False
       