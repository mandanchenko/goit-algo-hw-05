class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True

        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index in range(len(self.table[key_hash])):
                if self.table[key_hash][index][0] == key:
                    return self.table[key_hash].pop(index)
        return "Not found"


if __name__ == "__main__":
    # Тестуємо нашу хеш-таблицю:
    H = HashTable(7)
    H.insert("Harry", 150)
    H.insert("Hermiona", 30)
    H.insert("Ron", 45)
    H.insert("Sirius", 50)
    H.insert("Minerva", 100)
    H.insert("Fred", 60)
    H.insert("Jorje", 65)
    H.insert("Viktor", 75)
    H.insert("Igor", 90)
    H.insert("Albus", 107)
    H.insert("Persi", 17)
    H.insert("Luna", 125)
    H.insert("Nevil", 110)
    print(H.table)
    print(H.delete("Albus"))
    print(H.delete("Igor"))
    print(H.delete("Jorje"))
    print(H.delete("Lucius"))
    print(H.table)
