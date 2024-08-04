
class List_node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.most_searched_value = 0

    def insert(self, value):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = List_node(value)
        else:
            # primeira inserção
            self.head = List_node(value)

    def print_list(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next


