/***************Nodo***************/
function Node(value){
    this.value = value;

    this.left = null;
    this.right = null;
    this.parent = null;
}

/**Arbol Binario**/
function BST(){
    this.root = null;

    this.search = BSTSearch;
    this.delete = BSTDelete;
    this.print = BSTPrint;

    //Numerico
    this.addNumerically = BSTAddNumerically;
    this.searchNumerically = BSTSearchNumerically;
    this.deleteNumerically = BSTDeleteNumerically;

    //Alfabetico
    this.addAlphabetically = BSTAddAlphabetically;
    this.searchAlphabetically = BSTSearchAlphabetically;
    this.deleteAlphabetically = BSTDeleteAlphabetically;
}

    

    function BSTSearch(value, typeOfValue){
        if(typeOfValue == "number"){
            return this.searchNumerically(value);
        }
        else{
            return this.searchAlphabetically(value);
        }
    }

    function BSTDelete(value, typeOfValue){
        if(typeOfValue == "number"){
            return this.deleteNumerically(value);
        }
        else{
            return this.deleteAlphabetically(value);
        }
    }

    function BSTPrint(current = this.root, trail =""){
        if(current){
            if(current.left){
                this.print(current.left, trail);
            }
            trail = trail + current.value.name + ": " + current.value.number + "\n";

            if(current.right){
                this.print(current.right, trail);
            }
        }
    }
    
/***********Para el arbol ordenado numericamente*********************/
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
                        current.left.parent = current;
                        return true;
                    }
                }
                else{
                    if(current.right){
                        return this.addNumerically(newNode, current.right);
                    }
                    else{
                        current.right = newNode;
                        current.right.parent = current;
                        return true;
                    }
                }
            }
            return false;
    }

    function BSTSearchNumerically(value, current = this.root){
        if(!this.root){
            return null;
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
                    return null;
                }
            }

            else{
                if(current.right){
                    return this.searchNumerically(value, current.right);
                }
                else{
                    return null;
                }
            }
        }
    }


    function BSTDeleteNumerically(deleteValue){
        if(deleteValue == this.root.value.number){
            left = this.root.left;
            right = this.root.right;
            this.root = null;
            if(right){
                this.addNumerically(right);
            }
            if(left){
                this.addNumerically(left);
            }
            return true;
        }
        else{
            var parent = this.searchNumerically(deleteValue);
            if(parent.right){
                if(parent.right.value.number == deleteValue){
                        left = parent.right.left;
                        right = parent.right.right;
                        parent.right = null;
                    if(right){
                        this.addNumerically(right);
                    }
                    if(left){
                        this.addNumerically(left);
                    }
                    return true;
                }
            }
            else if(parent.left){
                if(parent.left.value.number == deleteValue){
                        left = parent.left.left;
                        right = parent.left.right;
                        parent.left = null;
                    if(right){
                        this.addNumerically(right);
                    }
                    if(left){
                        this.addNumerically(left);
                    }
                    return true;
                }
            }
        }
        return false;

    }

/***********Para el arbol ordenado alfabeticamente*********************/
function BSTAddAlphabetically(newNode, current = this.root){
    if(!this.root){
        this.root = newNode;
        return true;
    }

    else{
        if(current.value.name > newNode.value.name){
            if(current.left){
                return this.addAlphabetically(newNode, current.left);
            }
            else{
                current.left = newNode;
                return true;
            }
        }
        else{
            if(current.right){
                return this.addAlphabetically(newNode, current.right);
            }
            else{
                current.right = newNode;
                return true;
            }
        }
    }
    return false;
}

function BSTSearchAlphabetically(value, current = this.root){
if(!this.root){
    return null;
}
else{
    if(current.value.name == value){
        return current;
    }
    else if(current.value.name > value){
        if(current.left){
            return this.searchAlphabetically(value, current.left);
        }
        else{
            return null;
        }
    }

    else{
        if(current.right){
            return this.searchAlphabetically(value, current.right);
        }
        else{
            return null;
        }
    }
    }
}


function BSTDeleteAlphabetically(deleteValue){
if(deleteValue == this.root.value.name){
    left = this.root.left;
    right = this.root.right;
    this.root = null;
    if(right){
        this.addAlphabetically(right);
    }
    if(left){
        this.addAlphabetically(left);
    }
    return true;
}
else{
    var parent = this.searchAlphabetically(deleteValue);
    if(parent.right){
        if(parent.right.value.name == deleteValue){
                left = parent.right.left;
                right = parent.right.right;
                parent.right = null;
            if(right){
                this.addAlphabetically(right);
            }
            if(left){
                this.addAlphabetically(left);
            }
            return true;
        }
    }
    else if(parent.left){
        if(parent.left.value.name == deleteValue){
                left = parent.left.left;
                right = parent.left.right;
                parent.left = null;
            if(right){
                this.addAlphabetically(right);
            }
            if(left){
                this.addAlphabetically(left);
            }
            return true;
        }
    }
}
return false;

}    