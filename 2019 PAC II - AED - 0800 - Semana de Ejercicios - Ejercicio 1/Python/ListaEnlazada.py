#Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

#Lista Enlazada
class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def agregar(self, valor, posicion = None):
        return self.agregarEnLista(valor)

    def agregarEnLista(self, valor):
        
        if (not self.primero):
            self.primero = Nodo(valor)
            self.ultimo = self.primero
            self.tamaño += 1
            return True

        else:
            if(actual.siguiente):
                actual = actual.siguiente
                return self.agregarEnLista(valor, actual)

            else:
                actual.siguiente = Nodo(valor)
                self.tamaño += 1
                return True

        return False

"""
lista = ListaEnlazada()
print (lista.agregar(3))
print (lista.agregar(5))
print (lista.agregar("hola"))

print(lista.primero.siguiente.valor)
"""