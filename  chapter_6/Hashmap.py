class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        return hash(value) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))



    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v

        return default


    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


    def keys(self):
        return [k for bucket in self.table for k, v in bucket]

    def values(self):
        return [v for bucket in self.table for k, v in bucket]


    def items(self):
        return[(k, v) for bucket in self.table for k, v in bucket]


# Пример использования
my_hashmap = HashMap()
my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "Example City")
print("Keys:", my_hashmap.keys())  # Ожидаемый вывод: Keys: ['name', 'age', 'city']
print("Values:", my_hashmap.values())  # Ожидаемый вывод: Values: ['John', 25, 'Example City']
print("Items:",
      my_hashmap.items())  # Ожидаемый вывод: Items: [('name', 'John'), ('age', 25), ('city', 'Example City')]

# Доступ к значениям по ключу
print("Name:", my_hashmap.get("name"))  # Ожидаемый вывод: Name: John
print("Gender:", my_hashmap.get("gender", "Not specified"))  # Ожидаемый вывод: Gender: Not specified

# Удаление пары ключ-значение
my_hashmap.remove("age")
print("Keys after removing 'age':", my_hashmap.keys())  # Ожидаемый вывод: Keys after removing 'age': ['name', 'city']