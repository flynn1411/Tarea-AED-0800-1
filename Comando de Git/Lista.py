/***********************Nodo********************************/

class Nodo
    def __init__(self, valor):
    self.valor = valor
    self.siguiente = None


/*********************Lista Enlazada**************************/

class ListaEnlazada:
    def __init__(self):
        #atributo
        self.primero = None

        #metodos
        self.agregar = ListaEnlazadaAgregar
        self.agregarNormal = ListaEnlazadaAgregarNormal
        self.agregarEnPosicion = ListaEnlazadaAgregarEnPosicion
        self.obtenerTamaño = ListaEnlazadaObtenerTamaño
        self.imprimir = ListaEnlazadaImprimir

class ListaEnlazadaAgregar:
    
    def __init__(self,valor, posicion = None):

        if(not posicion):
            return self.agregarNormal(valor)
                
        else:
            return self.agregarEnPosicion(valor, posicion)

    
    def ListaEnlazadaAgregarNormal(self,valor, actual = self.primero):
     
        if(not self.primero):
            self.primero = Nodo(valor)
            return True
        
        elif(actual.siguiente):
            return self.agregarNormal(valor,actual.siguiente)
    
        else:
            actual.siguiente = Nodo(valor)
            return True
    
        return False

    
    def ListaEnlazadaAgregarEnPosicion(valor, posicion):
        if(posicion == 0):
            cola = self.primero
            self.primero = Nodo(valor)
            self.primero.siguiente = cola
            return True
        
        else
            if(posicion > self.obtenerTamaño()):
                return self.agregar(valor)
            
            else:
                actual = self.primero.siguiente
                anterior = self.primero
                posicionActual = 1

                while(actual.siguiente):
                    if(posicion == posicionActual):
                        anterior.siguiente = Nodo(valor)
                        anterior.siguiente.siguiente = actual
                        return True
                    
                    else:
                        anterior = actual
                        actual = actual.siguiente
            return False

    def ListaEnlazadaObtenerTamaño(self):
        contador = 1
        actual = self.primero

        while(actual.siguiente):
            actual = actual.siguiente
            contador += 1
        
        return contador

    def ListaEnlazadaImprimir(self):
        camino = " "
        actual = self.primero
    
        while(actual.siguiente):
            camino = camino + actual.valor + " -> "
            actual = actual.siguiente
        
        camino = camino + actual.valor + " -> NULL"
    
        print(camino)
    
    
    

        
        