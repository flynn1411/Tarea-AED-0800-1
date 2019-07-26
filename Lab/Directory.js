function Directory(){
    this.numericalTree = new BST();
    this.alphabeticalTree = new BST();

    this.mainMenu = DirectoryMainMenu;
    this.addPrompt = DirectoryAddPrompt;
    this.searchPrompt = DirectorySearchPrompt;
    this.deletePrompt = DirectoryDeletePrompt;
    this.printPrompt = DirectoryPrintPrompt;
}

    function DirectoryMainMenu(){
        
        this.continue = true;
        menu = "Directorio de Contactos\n\nSeleccione una opción:\n1.Agregar Contacto\n2.Buscar Contacto\n3.Borrar Contacto\n4.Mostrar Contactos\n5.Salir\n";

        while(this.continue){
            option = prompt(menu);

            switch(option){
                case "1":
                    this.addPrompt();
                    break;

                case "2":
                    this.searchPrompt();
                    break;

                case "3":
                    this.deletePrompt();
                    break;

                case "4":
                    this.printPrompt();
                    break;

                case "5":
                    document.write("Programa Finalizado.");
                    this.continue = false;
                    break;

                default:
                    mensaje = `La opción ingresada ${option} no está en el menú.`;
                    alert(mensaje);
                    break;
            }
        }

    }

    function DirectoryAddPrompt(){
        name = prompt("Ingrese el nombre:");
        number = prompt("Ingrese el número:");

        wasAddedNumerically = this.numericalTree.addNumerically(new Node(new Contact(name, number)));
        wasAddedAlphabetically = this.alphabeticalTree.addAlphabetically(new Node(new Contact(name, number)));

        if(wasAddedNumerically && wasAddedAlphabetically){
            prompt(`El contacto ${name}: ${number} fue agregado exitosamente.`);
        }
        else{
            prompt(`El contacto ${name}: ${number} ya existe`);
        }
    }

    function DirectorySearchPrompt(){
        alert("Buscando Nodo");
    }

    function DirectoryDeletePrompt(){
        alert("Borrando Nodo");
    }

    function DirectoryPrintPrompt(){
        printFormat = prompt("Desea verlo por:\n1.Orden Alfabético\n2.Orden Numerico");
        
        if(printFormat == "1"){
            this.alphabeticalTree.print();
        }
        else{
            this.numericalTree.print();
        }
    }

    