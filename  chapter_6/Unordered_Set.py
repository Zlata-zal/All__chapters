class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
        return hash(value) % self.size

    def add(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def remove(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def contains(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]
        return value in bucket

    def elements(self):
        all_elements = []
        for bucket in self.buckets:
            all_elements.extend(bucket)
        return all_elements


my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements:", my_set.elements())

# Check if a value is in the set
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

# Remove a value from the set
value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())