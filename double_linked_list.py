class DLL_node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tailer = None

    def insert_on_head(self, value):
        node = DLL_node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def print_list(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next
