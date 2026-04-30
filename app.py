class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# ======================
# TEST
# ======================
ht = HashTable()

ht.insert("nama", "Budi")
ht.insert("umur", 20)
ht.insert("kota", "Bandung")

print("Hasil Search:")
print("nama:", ht.search("nama"))
print("umur:", ht.search("umur"))

print("\nIsi Hash Table:")
ht.display()
