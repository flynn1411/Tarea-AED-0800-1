/***********************Nodo********************************/

function Nodo(valor){
    this.valor = valor;
    this.siguiente = null;
}

/*********************Lista Enlazada**************************/

function ListaEnlazada(){
    //atributo
    this.primero = null;

    //metodos
    this.agregar = ListaEnlazadaAgregar;
    this.agregarNormal = ListaEnlazadaAgregarNormal;
    this.agregarEnPosicion = ListaEnlazadaAgregarEnPosicion;
    this.obtenerTamaño = ListaEnlazadaObtenerTamaño;
    this.imprimirLista = ListaEnlazadaImprimir;
}

    function ListaEnlazadaAgregar(valor, posicion = null){
        if(posicion == null){
            return this.agregarNormal(valor);
        }
        else{
            return this.agregarEnPosicion(valor, posicion);
        }
    }

    function ListaEnlazadaAgregarNormal(valor, actual = this.primero){
        if(!this.primero){
            this.primero = new Nodo(valor);
            return true;
        }

        else{
            if(actual.siguiente){
                return this.agregarNormal(valor, actual.siguiente);
            }

            else{
                actual.siguiente = new Nodo(valor);
                return true;
            }
        }
        return false;
    }

    function ListaEnlazadaAgregarEnPosicion(valor, posicion){
        if(posicion == 0){
            cola = this.primero;
            this.primero = new Nodo(valor);
            this.primero.siguiente = cola;
            return true;
        }
        else{
            if(posicion > this.obtenerTamaño()){
                return this.agregar(valor);
            }
            else{
                actual = this.primero;
                anterior = null;
                posicionActual = 0;

                while(actual){
                    if(posicion == posicionActual){
                        anterior.siguiente = new Nodo(valor);
                        anterior.siguiente.siguiente = actual;
                        return true;
                    }
                    else{
                        anterior = actual;
                        actual = actual.siguiente;
                        posicionActual++;
                    }
                }
            }
            return false;
        }
    }

    function ListaEnlazadaObtenerTamaño(){
        contador = 1;
        actual = this.primero;

        while(actual.siguiente){
            actual = actual.siguiente;
            contador++;
        }

        return contador;
    }

   function ListaEnlazadaImprimir(){
        camino = " ";
    
        nodoActual = this.primero;
    
        while(nodoActual.siguiente){
            camino = camino + nodoActual.valor + " -> ";
    
            nodoActual = nodoActual.siguiente;
        }
    
        camino = camino + nodoActual.valor + " -> NULL";
    
        console.log(camino);
    }