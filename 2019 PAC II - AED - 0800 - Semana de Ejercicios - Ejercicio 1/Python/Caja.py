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
        grupoActual = self.primerGrupo

        while(grupoActual.siguiente):
            grupoActual.valor.imprimirLista()
            print("\n")
            grupoActual = grupoActual.siguiente
        
        grupoActual.valor.imprimirLista()