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
            alert(`El contacto ${name}: ${number} fue agregado exitosamente.`);
        }
        else{
            alert(`El contacto ${name}: ${number} ya existe`);
        }
    }

    function DirectorySearchPrompt(){
        wasFound = null;
        searchBy = prompt("Desea buscar el contacto por:\n1.Nombre\n2.Número");
        if(searchBy == "1"){
            searchValue = prompt("Ingrese el nombre:");
            wasFound = this.alphabeticalTree.searchAlphabetically(searchValue);
        }
        else{
            searchValue = prompt("Ingrese el número:");
            wasFound = this.numericalTree.searchNumerically(searchValue);
        }

        if(wasFound){
            alert(`${wasFound.value.name}: ${wasFound.value.number}`);
        }
        else{
            alert(`El contacto no existe en el directorio.`);
        }
    }

    function DirectoryDeletePrompt(){
        wasDeleted = null;
        deleteBy = prompt("Desea borrar el contacto por:\n1.Nombre\n2.Número");
        if(deleteBy == "1"){
            deleteValue = prompt("Ingrese el nombre:");
            wasDeleted = this.alphabeticalTree.deleteAlphabetically(deleteValue);
        }
        else{
            deleteValue = prompt("Ingrese el número:");
            wasDeleted = this.numericalTree.deleteNumerically(deleteValue);
        }

        if(wasDeleted){
            alert(`El contacto deseado fue borrado.`);
        }
        else{
            alert(`El contacto no existe en el directorio.`);
        }

    }

    function DirectoryPrintPrompt(){
        printFormat = prompt("Desea verlo por:\n1.Orden Alfabético\n2.Orden Numerico");
        var tree = "";

        if(printFormat == "1"){
            tree = this.alphabeticalTree.print();
        }
        else{
            tree = this.numericalTree.print();
        }

        if(tree == ""){
            alert("El directorio está vacio.");
        }
        else{
            alert(tree);
        }
    }

    