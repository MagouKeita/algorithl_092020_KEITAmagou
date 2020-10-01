from typing import list, Dict

class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """




    def insert(self, value: int) -> None:
       # Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        #Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
       # Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
       # Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
      #  Fusionne deux arbres
        """
        pass


class FibonacciHeap(Heap):
    """
   # Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement

   # https://en.wikipedia.org/wiki/Fibonacci_heap

   # L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
   # et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    

#first heap (premiere arbre)

fib_heap= FibonacciHeap()
fib_heap.insert(0)
fib_heap.insert(2)
fib_heap.insert(4)
fib_heap.insert(6)

#second heap (deuxieme arbre)

fib2_heap= FibonacciHeap()
fib2_heap.insert(1)
fib2_heap.insert(3)
fib2_heap.insert(5)
fib2_heap.insert(7)

class node:
    def _init_(self,value,clef):
        self.value = value
        self.parents= self.children = None
        self.left= self.right= None
        self.clef= clef
root_node= None
min_node= None
total_nodes=0

    def insert(self, value: int) -> None:
        insert_a_node=self.node(value)
        insert_a_node.left=insert_a_node
        insert_a_node.right= insert_a_node

        if self.root_node=None
            self.root_node=insert_a_node
        else:
            insert_a_note.right=self.root_node.right
            insert_a_note.left=self.root_node
            self.root_node.right +self.root_node.left=insert_a_node
        
        if self.min_node=None:
            self.min_node= insert_a_node

        if insert_a_node<self.min_node.value:
            self.min_node=insert_a_node
        
        sel.total_nodes +=1
        return insert_a_node

   def find_min(self) -> int:
        """
     Retourne la valeur minimum dans l'arbre
        """
        return self.min_node.value

    def delete_min(self) -> int:
       min= self.min_node
      Supprime et retourne la valeur minimum dans l'arbre
        if self.root_node = None:
            self.root_node = min.child
        else:
            min.right = self.root_node.right
            min.left = self.root_node
            self.root_node.right.left = min.child
            self.root_node.right = min.child
        

    def merge(self, fibonnaci_heap: Heap) -> None:
        
        Fibh = FibonacciHeap()
        Fibh.root_node, Fibh.min_node = self.root_node, self.min_node
       
        last = fibonnaci_heap.root_node.left
        fibonnaci_heap.root_node.left = FileExistsError.root_node.left
       
        Fibh.root_node.left.right = fibonnaci_heap.root_node
        Fibh.root_node.left = last
        Fibh.root_node.left.right = Fibh.root_node

        if fibonnaci_heap.min_node.value < Fibh.min_node.value:
            Fibh.min_node = fibonnaci_heap.min_node
        Fibh.total_nodes = self.total_nodes + fibonnaci_heap.total_nodes
        return Fibh
        

