class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def in_order_traversal(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result


    def pre_order_traversal(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def post_order_traversal(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result


# Пример использования
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))  # Ожидаемый вывод: <__main__.TreeNode object at ...>
print(tree.search(20))  # Ожидаемый вывод: None

print(tree.in_order_traversal())  # Ожидаемый вывод: [5, 10, 15]
print(tree.pre_order_traversal())  # Ожидаемый вывод: [10, 5, 15]
print(tree.post_order_traversal())  # Ожидаемый вывод: [5, 15, 10]
