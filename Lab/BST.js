/***************Nodo***************/
function Node(value){
    this.value = value;
    this.left = null;
    this.right = null;
}

/**Arbol Binario**/
function BST(){
    this.root = null;

    this.search = BSTSearch;
    //this.print = BSTPrint;

    //Numerico
    this.addNumerically = BSTAddNumerically;
    this.searchNumerically = BSTSearchNumerically;
    this.deleteNumerically = BSTDeleteNumerically;

    //Alfabetico
    //this.addAlphabetically = BSTAddAlphabetically;
    //this.searchAlphabetically = BSTSearchAlphabetically;
    //this.deleteAlphabetically = BSTDeleteAlphabetically;
}

    function BSTAddNumerically(newNode, current = this.root){
        if(!this.root){
            this.root = newNode;
            return true;
        }

        else{
            if(current.value.number > newNode.value.number){
                if(current.left){
                    return this.addNumerically(newNode, current.left);
                }
                else{
                    current.left = newNode;
                    return true;
                }
            }
            else{
                if(current.right){
                    return this.addNumerically(newNode, current.right);
                }
                else{
                    current.right = newNode;
                    return true;
                }
            }
        }
        return false;
    }

    function BSTSearch(value, typeOfValue){
        if(typeOfValue == "number"){
            return this.searchNumerically(value);
        }
        else{
            return this.searchAlphabetically(value);
        }
    }

    function BSTSearchNumerically(value, current = this.root){
        if(!this.root){
            return true;
        }
        else{
            if(current.value.number == value){
                return current;
            }
            else if(current.value.number > value){
                if(current.left){
                    return this.searchNumerically(value, current.left);
                }
                else{
                    return false;
                }
            }

            else{
                if(current.right){
                    return this.searchNumerically(value, current.right);
                }
                else{
                    return false;
                }
            }
        }
    }


    function BSTDeleteNumerically(value, current = this.root){
        if(!this.root){
            return false;
        }
        else if(this.searchNumerically(value)){
            return false;
        }
        else{
            if(this.root.value.number == value){
                leftChildren = this.root.left;
                rightChildren = this.root.right;

                this.root = null;

                if(rightChildren){
                    this.addNumerically(rightChildren);
                }
                if(leftChildren){
                    this.addNumerically(leftChildren);
                }
                return true;
            }

            else if(current.value.number > value){
                if(current.left){
                    if(current.left.value.number == number){
                        leftChildren = current.left;
                        rightChildren = current.right;

                        current.left = null;

                        if(rightChildren){
                            this.addNumerically(rightChildren);
                        }
                        if(leftChildren){
                            this.addNumerically(leftChildren);
                        }
                        return true;
                    }
                    else{
                        return this.deleteNumerically(value, current.left);
                    }
                }
            }

            else{
            if(current.value.number > value){
                if(current.right){
                    if(current.right.value.number == number){
                        leftChildren = current.left;
                        rightChildren = current.right;

                        current.right = null;

                        if(rightChildren){
                            this.addNumerically(rightChildren);
                        }
                        if(leftChildren){
                            this.addNumerically(leftChildren);
                        }
                        return true;
                    }
                    else{
                        return this.deleteNumerically(value, current.right);
                        }
                    }
                }
            } 
        }
    }