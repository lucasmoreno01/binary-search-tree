from linked_list import List_node, LinkedList
from double_linked_list import DLL_node, DoubleLinkedList


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.searched = 0


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.linked_list = LinkedList()
        self.d_linked_list = DoubleLinkedList()

    def insert(self, value):
        parent = None
        current = self.root
        while current:
            parent = current
            if value == current.data:
                print(f"palavra ja existente: {value}")
                return
            elif value < current.data:
                current = current.left
            else:
                current = current.right

        if parent is None:
            self.root = Node(value)
            print(f"palavra inserida: {value}")
        elif value < parent.data:
            parent.left = Node(value)
            print(f"palavra inserida: {value}")
        else:
            parent.right = Node(value)
            print(f"palavra inserida: {value}")

    def search(self, value):
        if self.root is not None:
            current = self.root
            while current:
                if value < current.data:
                    current = current.left
                elif value > current.data:
                    current = current.right
                else:
                    current.searched += 1
                    print(f"palavra existente: {current.data} {current.searched}")
                    return current

        print(f"palavra inexistente: {value}")
        return None

    def _get_most_consulted_value(self, node):
        if node is None:
            return 0  

        left_count = self._get_most_consulted_value(node.left)
        right_count = self._get_most_consulted_value(node.right)

        if node.searched >= left_count and node.searched >= right_count:
            return node.searched
        elif left_count >= right_count:
            return left_count
        else:
            return right_count

    def _print_most_consulted_values(self, nconsult, node):
        if node is None:
            return

        if node.left:
            self._print_most_consulted_values(nconsult, node.left)

        if node.searched == nconsult:
            print(node.data)

        if node.right:
            self._print_most_consulted_values(nconsult, node.right)

    def show_most_consulted(self):
        if self.root is None:
            print('arvore vazia')
            return

        count = self._get_most_consulted_value(self.root)
        print("palavras mais consultadas:")
        self._print_most_consulted_values(count, self.root)
        print(f"numero de acessos: {count}")

    def remove(self, value, node="ROOT"):
        if node == "ROOT":
            node = self.root

        if node is None:
            print(f"palavra inexistente: {value}")
            return None

        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                print(f"palavra removida: {node.data}")
                if node == self.root:
                    self.root = node.right
                return node.right
            elif node.right is None:
                print(f"palavra removida: {node.data}")
                if node == self.root:
                    self.root = node.left
                return node.left
            else:
                
                successor_parent = node
                successor = node.right
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

                node.data = successor.data
                node.searched = successor.searched

                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
                print(f"palavra removida: {value}")

        return node

    def showInorderTree(self, l1, l2):
        self.linked_list.head = None
        print('palavras em ordem:')
        if self.root is not None:
            self._inorderTree(self.root, l1, l2)
            if self.linked_list.head is not None:
                self.linked_list.print_list()
                return
            else:
                print("lista vazia")
                return
        else:
            print("lista vazia")
            return

    def _inorderTree(self, node, l1, l2):
        if node.left:
            self._inorderTree(node.left, l1, l2)

        if l1 <= node.data[0] <= l2:
            self.linked_list.insert(node.data)
        if node.right:
            self._inorderTree(node.right, l1, l2)

    def showLevel(self, level):
        if self.root is not None:
            if level <= self._height() and level >= 1:
                print(f'palavra no nivel: {level}')
                self._getTreeLevel(self.root, level)
                return
        print(f'nao ha nos com nivel: {level}')
        return

    def _getTreeLevel(self, node, level):
        if node is None:
            return

        if level == 1:
            print(node.data)
            return

        self._getTreeLevel(node.left, level - 1)
        self._getTreeLevel(node.right, level - 1)

    def _height(self, node=None):
        if self.root is not None:
            if node is None:
                node = self.root
            hleft = 0
            hright = 0
            if node.left:
                hleft = self._height(node.left)
            if node.right:
                hright = self._height(node.right)
            if hright > hleft:
                return hright + 1
            return hleft + 1

    def travessal(self, value):
        self.d_linked_list.head = None
        if self.root is not None:
            current = self.root
            found = False
            while current:
                if value < current.data:
                    current = current.left
                elif value > current.data:
                    current = current.right
                else:
                    found = True
                    break

            if found:
                current = self.root
                while current:
                    self.d_linked_list.insert_in_order(current.data)
                    if value < current.data:
                        current = current.left
                    elif value > current.data:
                        current = current.right
                    else:
                        break

                print("palavras no caminho:")
                self.d_linked_list.print_list()
                return

        print(f"palavra inexistente: {value}")
        return

    def print_tree(self, node):
        if self.root is None:
            print('arvore vazia')
            return
        if node is None:
            return
        left_value = node.left.data if node.left is not None else "nil"
        right_value = node.right.data if node.right is not None else "nil"
        print(f"palavra: {node.data} freq: {node.searched} fesq: {left_value} fdir: {right_value}")
        self.print_tree(node.left)
        self.print_tree(node.right)
