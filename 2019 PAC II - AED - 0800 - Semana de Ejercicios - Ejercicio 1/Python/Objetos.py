#Objetos

class Lapiz:
    def __init__(self,marca, tipo):
        self.marca = marca
        self.tipo = tipo

class ResmaDePapel:
    def __init__(self, marca, tipo, cantidad):
        self.marca = marca
        self.tipo = tipo
        self.cantidad = cantidad
        #altura depende del tipo de papel

class Clips:
    def __init__(self, cantidad, tamañoClip):
        self.cantidad = cantidad
        self.tamañoClip = tamañoClip
        self.altura = 0
        self.longitud = 0

class Grapadora:
    def __init__(self, marca, capacidad):
        self.marca = marca
        self.capacidad = capacidad

class Grapas:
    def __init__(self, cantidad, tamañoGrapa):
        self.cantidad = cantidad
        self.tamañoGrapa = tamañoGrapa

class Folder:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

class PostIts:
    def __init__(self, color, cantidad):
        self.color = color
        self.cantidad = cantidad

class Marcador:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

class Borrador:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

class Corrector:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

class CintaAdhesiva:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo