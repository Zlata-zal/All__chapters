class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if self.is_empty():
            raise IndexError("Heap is empty")

        root = self.heap[0]
        last_item = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_item
            self._heapify_down(0)

        return root

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        while left_child_index < size:
            swap_index = left_child_index
            if right_child_index < size and self._compare(self.heap[right_child_index], self.heap[left_child_index]):
                swap_index = right_child_index


            if self._compare(self.heap[index], self.heap[swap_index]):
                break

            self.heap[index], self.heap[swap_index] = self.heap[swap_index], self.heap[index]

            index = swap_index
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

# Пример использования
h = Heap(max_heap=True)  # Создаем максимальную кучу

# Вставка элементов
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())  # Ожидаемый вывод: 20

# Извлечение корней
while not h.is_empty():
	print("Извлеченный элемент:", h.extract())
