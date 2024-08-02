from word_bst import BinarySearchTree


# versão do python: 3.12.3



bst = BinarySearchTree()


while True:
    cmd = str(input())
    
    if cmd == "e":
        break

    match cmd:
        case "i":
            value = str(input())
            bst.insert(value)
        
        case "c":
            value = str(input())
            bst.search(value)
        
        case "f":
            bst.show_most_consulted()
        
        case "o":
            l1 = str(input())
            l2 = str(input())
            bst.showInorderTree(l1, l2)
        
        case "r":
            value = str(input())
            bst.remove(value)
        
        case "n":
            level = int(input())
            bst.showLevel(level) # TODO: corrigir erro
        
        case "t":
            value = str(input())
            bst.travessal(value)
        
        case "p":
            bst.showTree(bst.root)  # TODO: corrigir erro
        
        case _:
            print("comando invalido")



# bst.root = Node("Rodrigo")

# bst.insert("Lucas")
# bst.insert("Lucas")  # palavra ja existente
# bst.insert("Ze")
# bst.insert("Alice")
# bst.insert("Xuxa")
# bst.insert("Ziraldo")
# bst.insert("Lucca")

