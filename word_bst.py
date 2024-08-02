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
        self.order_list = LinkedList()
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
                    print(f"palavra existente: {
                          current.data} {current.searched}")
                    self._q_search_increment(current)
                    return current

        print(f"palavra inexistente: {value}")
        return None

    def _q_search_increment(self, node):
        if node.searched == self.linked_list.most_searched_value or self.linked_list.head is None:
            self.linked_list.insert(node.data)
        elif node.searched > self.linked_list.most_searched_value and self.linked_list.head is not None:
            if self.linked_list.head.next:
                self.linked_list.head = node
                self.linked_list.head.next = None
                self.linked_list.size = 1
            self.linked_list.most_searched_value = node.searched

        return node

    def _treeTravessal(self, node):
        if node is None:
            return node
        self._treeTravessal(node.left)
        self._treeTravessal(node.right)

    def show_most_consulted(self):

        if self.root is not None:
            if self.linked_list.head is not None:
                print('palavras mais consultadas:')
                self.linked_list.print_list()

            else:
                self._treeTravessal(self.root)
            print(f'numero de acessos: {
                      self.linked_list.most_searched_value}')
            return
        print("arvore vazia")

    def remove(self, value, node="ROOT"):
        if node == "ROOT":
            node = self.root

        if node is None:
            print("palavra nao encontrada")
            return node

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
                # Encontrar o menor nó na subárvore direita (sucessor)
                successor_parent = node
                successor = node.right
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

                # Substituir os dados do nó pelo sucessor
                node.data = successor.data

                # Remover o sucessor
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
                print(f"palavra removida: {value}")

                # Remove word from the most consulted list
                self.linked_list.remove(value)

        return node

    def showInorderTree(self, l1, l2):
        self.order_list.clear()  # Clear the list before populating it again
        if self.root is not None:
            self._inorderTree(self.root, l1, l2)
            if self.order_list.head is not None:
                print('palavras em ordem:')
                self.order_list.print_list()
            else:
                print("lista vazia")
        else:
            print("arvore vazia")

    def _inorderTree(self, node, l1, l2):
        if node.left:
            self._inorderTree(node.left, l1, l2)

        if node.data[0] >= l1 and node.data[0] <= l2:
            self.order_list.insert(node.data)
        if node.right:
            self._inorderTree(node.right, l1, l2)

    def showLevel(self, level):
        if self.root is not None:
            if level > self._height():
                print(f'nao ha nos com nivel: {level}')
                return
            if self.root is not None:
                print(f'palavra no nivel: {level}')
                self._getTreeLevel(self.root, level)

    def _getTreeLevel(self, node, level):
        if level == 1:
            if node is not None:
                print(node.data)
                return node

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

                print("palavras no caminho")
                self.d_linked_list.print_list()
                return current

        print(f"palavra nao existente {value}")
        return None

    def showTree(self, node):
        if self.root is None:
            print('arvore vazia')
        if node is None:
            return node
        left_value = node.left.data if node.left is not None else "nill"
        right_value = node.right.data if node.right is not None else "nill"
        print(f"palavra: {node.data} freq: {node.searched} fesq: {
              left_value} fdir: {right_value}")
        self.showTree(node.left)
        self.showTree(node.right)
