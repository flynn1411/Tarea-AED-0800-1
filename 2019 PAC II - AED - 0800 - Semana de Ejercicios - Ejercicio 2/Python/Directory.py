from BST import*
from Contact import*

class Directory:
    def __init__(self):
        self.numericalTree = BST()
        self.alphabeticalTree = BST()

    def DirectoryAddinput(self):
        name = input("Ingrese el nombre:")
        number = input("Ingrese el número:")

        wasAddedNumerically = self.numericalTree.addNumerically(Node(Contact(name,number)))
        wasAddedAlphabetically = self.alphabeticalTree.addAlphabetically(Node(Contact(name,number)))

        if(wasAddedNumerically and wasAddedAlphabetically):
            input("El contacto %s: %s fue agregado exitosamente."%(name,number))
        
        else:
            input("El contacto %s: %s ya existe"%(name,number))
    
    
    def mainMenu(self):
       
        menu = """Directorio de Contactos:
        1.Agregar Contacto
        2.Buscar Contacto
        3.Borrar Contacto
        4.Mostrar Contactos
        5.Salir
        """

        Keep = True
        while(Keep):

            print("\n" + menu)

            eleccion = input("Elige: ")
            if eleccion is "1":
                print("Insertar")


            elif eleccion is "2":
                print("Ver")


            elif eleccion is "3":
                print("Actualizar")


            elif eleccion is "4":
                print("Eliminar")


            elif eleccion is "5":
                print("Salir")
                Keep = False
            else:
                #Equivalente a 'default'
                print("Ninguna opción válida seleccionada")


Prueba = Directory()
Prueba.mainMenu()