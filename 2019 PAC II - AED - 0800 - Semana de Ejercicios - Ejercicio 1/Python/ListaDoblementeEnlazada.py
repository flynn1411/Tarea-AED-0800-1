#Nodo
class Nodo:
    def __init__(self, valor, posicion):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
        self.posicion = posicion

#Lista Enlazada
class ListaDoblementeEnlazada:
    def __init__(self, limiteTamaño):
        self.primero = None
        self.ultimo = None
        self.tamaño = 0
        self.limiteTamaño = limiteTamaño

    def agregar(self, valor, posicion = None):
        return self.agregarEnLista(valor)

    def agregarEnLista(self, valor):
        
        if (not self.primero):
            self.primero = Nodo(valor, self.tamaño)
            self.ultimo = self.primero
            self.tamaño += 1
            return True

        else:
            self.ultimo.siguiente = Nodo(valor, self.tamaño)
            self.ultimo.siguiente.anterior = self.ultimo
            self.ultimo = self.ultimo.siguiente
            self.tamaño += 1

        return False

    def agregarEnPosicion(self, valor, posicion):
        
        actual = self.primero
        contador = 0

        if(not self.primero):
            comodin = Nodo(0,contador)
            contador += 1

        else:
            while (contador < posicion):
                
                comodin = Nodo(0,contador)
                
                if(posicion == actual.posicion):
                    
                    if(actual.valor == comodin):
                        actual = Nodo(valor, posicion)
                        return True 
                    else:    
                        return False
                
                elif(not actual.siguiente):
                    actual.siguiente = comodin
                    
            actual = actual.siguiente
            contador += 1
        
        




            

"""
lista = ListaEnlazada()
print (lista.agregar(3))
print (lista.agregar(5))
print (lista.agregar("hola"))

print(lista.primero.siguiente.valor)
"""