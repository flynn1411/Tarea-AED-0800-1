# -*-coding: "utf-8" -*-
#/***********************Nodo********************************/

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


#/*********************Lista Enlazada**************************/

class ListaEnlazada:
    def __init__(self):
        #atributo
        self.primero = None
             
    def agregar(self,valor, posicion = None):

        if(posicion is None):
            return self.agregarNormal(valor, self.primero)
                
        else:
            return self.agregarEnPosicion(valor,posicion)

    
    def agregarNormal(self,valor, actual = None):
        
        if(not self.primero):
            self.primero = Nodo(valor)
            return True
        
        elif(actual.siguiente):
            return self.agregarNormal(valor,actual.siguiente)
    
        else:
            actual.siguiente = Nodo(valor)
            return True
    
        return False

    
    def agregarEnPosicion(self,valor, posicion):
       
        if(posicion == 0):
            cola = self.primero
            self.primero = Nodo(valor)
            self.primero.siguiente = cola
            return True
        
        else:
            if(posicion > self.obtenerLongitud()):
                return self.agregar(valor)
            
            else:
                actual = self.primero
                anterior = None
                posicionActual = 0

                while(actual):
                    if(posicion == posicionActual):
                        anterior.siguiente = Nodo(valor)
                        anterior.siguiente.siguiente = actual
                        return True
                    
                    else:
                        anterior = actual
                        actual = actual.siguiente
                        posicionActual += 1
            return False

    def obtenerLongitud(self):
        contador = 1
        actual = self.primero

        while(actual.siguiente):
            actual = actual.siguiente
            contador += 1
        
        return contador

    def imprimirLista(self):
        camino = ""
        nodoActual = self.primero
    
        while(nodoActual.siguiente):
            camino = ("%s%s -> " %(camino, nodoActual.valor))
            nodoActual = nodoActual.siguiente
        
        camino = ("%s%s -> None" %(camino, nodoActual.valor))
    
        print(camino)
    
    
    
