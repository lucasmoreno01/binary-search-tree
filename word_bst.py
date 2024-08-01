from linked_list import List_node, LinkedList

# TODO: Apagar comentarios
# TODO: Checkar a operação com if/else ou mach/case
# TODO: Em caso de arvore vazia
# TODO: Em caso de item único

# Python 3.12.3


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

    def insert(self, value):
        parent = None
        current = self.root
        while current:
            parent = current
            if value < current.data:
                current = current.left
            else:
                current = current.right

        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

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

    def show_most_consulted(self):
        if self.root is not None:
            print('palavras mais consultadas:')
            self.linked_list.print_list()
            print(f'numero de acessos: {
                  self.linked_list.most_searched_value}')

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

        return node

    def showInorderTree(self, l1, l2):
        if self.root is not None:
            print('palavras em ordem:', end=" ")
            self._inorderTree(self.root, l1, l2)
        else:
            print("lista vazia")

    def _inorderTree(self, node, l1, l2):

        if node.left:
            self._inorderTree(node.left, l1, l2)

        if node.data[0] >= l1 and node.data[0] <= l2:
            print(node.data, end=" ")
        if node.right:
            self._inorderTree(node.right, l1, l2)

        return node

    def showLevel(self, level):
        if level > self._height():
            print(f'nao ha nos com nivel: {level}')
            return
        if self.root is not None:
            print(f'palavra no nivel: {level}')
            self._getTreeLevel(self.root, level)

    def _getTreeLevel(self, node, level):

        if level == 1:
            print(node.data)
            return node

        self._getTreeLevel(node.left, level - 1)
        self._getTreeLevel(node.right, level - 1)

    def _height(self, node=None):
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
        # if self.root is not None:
        #     current = self.root
        #     while current:
        #         self.path_list.insert(current.data)
        #         if value < current.data:
        #             current = current.left
        #         elif value > current.data:
        #             current = current.right
        #         else:
        #             self.path_list.print_list()
        #             return current

        return None


bst = BinarySearchTree()
bst.root = Node("Rodrigo")

bst.insert("Lucas")
bst.insert("Zé")
bst.insert("Alice")
bst.insert("Xuxa")


print(bst.root.data)
print(bst.root.left.data)
print(bst.root.right.data)

print('---------------------------------------')
bst.search("Lucas")
bst.search("Lucas")

bst.search("Alice")
bst.search("Alice")
bst.search("Lucas")
bst.search("Alice")


# bst.remove("Lucas")

print('---------------------------------------')
# print("Root:", bst.root.data)

print('---------------------------------------')

bst.showInorderTree('L', 'X')

print('\n ---------------------------------------')

bst.showLevel(2)

print('\n ---------------------------------------')
bst.show_most_consulted()

print('\n ---------------------------------------')
bst.travessal("Alice")
