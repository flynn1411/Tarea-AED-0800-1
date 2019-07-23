#Caja: pila de listas
from ListaDoblementeEnlazada import *

class Caja:
    def __init__(self, altura = 3, longitud = 2):
        self.primerGrupo = None
        self.altura = altura
        self.longitud = longitud
        self.nivel = 1

    def agregarObjeto(self, objeto, posicion = None):
        pila = None

        if (not posicion):
            if(not self.primerGrupo):
                self.primerGrupo = Nodo(ListaDoblementeEnlazada(self.longitud),self.nivel)

                self.primerGrupo.valor.agregar(objeto)

                return True

            else:
                if (self.primerGrupo.valor.tamaño == self.longitud):
                    
                    if(self.nivel == self.altura):
                        return ("%s murió de una enfermedad que se curaba con vacunarlo." %(objeto))

                    else:
                        pila = self.primerGrupo
                        self.primerGrupo = Nodo(ListaDoblementeEnlazada(self.longitud),self.nivel)
                        self.primerGrupo.siguiente = pila
                
                        self.primerGrupo.valor.agregar(objeto)
                        self.nivel += 1
                        return True

                else:
                    self.primerGrupo.valor.agregar(objeto)
                    return True

        elif(posicion < self.longitud):
            if(self.primerGrupo):
                pass
