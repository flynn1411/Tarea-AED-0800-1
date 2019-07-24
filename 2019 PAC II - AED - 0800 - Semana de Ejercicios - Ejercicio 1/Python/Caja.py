from Lista import*

class Caja:
    
    def __init__(self):
        self.primerGrupo = None
    
    def agregarFila(self):
        
        if(not self.primerGrupo):
            self.primerGrupo = Nodo(ListaEnlazada())
            return True
        
        else:
            pila = self.primerGrupo
            self.primerGrupo = Nodo(ListaEnlazada())
            self.primerGrupo.siguiente = pila
            return True
        
        return False

    def agregarObjeto(self,valor, posicion = None):
        return self.primerGrupo.valor.agregar(valor, posicion)
    
    def imprimirCaja(self):
        camino = ""
        actual = self.primerGrupo
    
        while(actual.siguiente):
            camino = ("%s%s -> " %(camino, actual.valor))
            actual = actual.siguiente
        
        camino = ("%s%s -> None" %(camino, actual.valor))
    
        print(camino)
    




    