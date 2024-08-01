class DLL_node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def insert_in_order(self, value):
        node = DLL_node(value)
        if self.head is None:
            # Lista está vazia
            self.head = node
            self.rear = node
        else:
            current = self.head
            while current is not None and current.data < value:
                current = current.next
            if current is None:
                # Inserir no final da lista
                self.rear.next = node
                node.prev = self.rear
                self.rear = node
            elif current == self.head:
                # Inserir no início da lista
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                # Inserir no meio da lista
                previous = current.prev
                previous.next = node
                node.prev = previous
                node.next = current
                current.prev = node


    def print_list(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next
