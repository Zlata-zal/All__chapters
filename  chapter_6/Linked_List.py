class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def delete(self, data):
    if self.is_empty():
        print("Список пуст, удаление невозможно.")
        return
    if current:
        previous.next = current.next
    else:
        print(f"Узел с данными {data} не найден.")

    def display(self):
        if self.is_empty():
            print("Список пуст.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next


# Example usage:
my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.prepend(0)

my_linked_list.display()

my_linked_list.delete(2)

my_linked_list.display()