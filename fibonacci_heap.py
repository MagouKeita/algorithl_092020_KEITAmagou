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
    """

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
        insert_a_node=self.node(clef,value)
        insert_a_node.left=insert_a_node
        insert_a_node.right= insert_a_node

        if self.root_node=None
            self.root_node=insert_a_node
        else:
            insert_a_note.right=self.root_node.right
            insert_a_note.left=self.root_node
            self.root_node.right +self.root_node.left=insert_a_node
        
        if self.min_node=None
            self.min_node= insert_a_node
    def find_min(self) -> int:
        """
     Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
      Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
      Fusionne deux arbres
        """
        pass

