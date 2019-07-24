function Caja(){
    //atributos
    this.primerGrupo = null;

    //metodos
    this.agregarFila = CajaAgregarFila;
    this.agregarObjeto = CajaAgregarObjeto;
    this.imprimir = CajaImprimir;
}

    function CajaAgregarFila(){
        if(!this.primerGrupo){
            this.primerGrupo = new Nodo(new ListaEnlazada());
            return true;
        }
        else{
            pila = this.primerGrupo;
            this.primerGrupo = new Nodo(new ListaEnlazada())
            this.primerGrupo.siguiente = pila;
            return true;
        }
        return false;
    }

    function CajaAgregarObjeto(valor, posicion = null){
        return this.primerGrupo.valor.agregar(valor, posicion);
    }

    function CajaImprimir(){
        grupoActual = this.primerGrupo;

        while(grupoActual.siguiente){
            grupoActual.valor.imprimirLista();
            grupoActual = grupoActual.siguiente;
        }
        grupoActual.valor.imprimirLista();
    }