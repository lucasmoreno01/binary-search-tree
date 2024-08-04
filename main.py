
# versão do Python: 3.12.3

from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()

cmd = " "

while cmd != "e" :
    cmd = str(input())
    

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
            bst.showLevel(level) 
        
        case "t":
            value = str(input())        
            bst.travessal(value) 
        
        case "p":
            bst.print_tree(bst.root)  
        
  



