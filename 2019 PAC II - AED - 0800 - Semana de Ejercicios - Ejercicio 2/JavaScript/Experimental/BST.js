/***********************Nodo*************************/
function Node(value){
		this.value = value;
		this.left = null;
		this.right = null;
    }
    
/**********************Arból Binario******************/
function BST(){
	this.root = null;

	this.add = BSTAdd;
	this.search = BSTSearch;
	this.print = BSTPrint;
	this.delete = BSTDeleteContact;
}

	function BSTAdd(newNode, current = this.root){
		if(!this.root){
			this.root = newNode;
			return true;
		}else{
			//Si la raiz es mayor que el valor a agregar
			if(current.value.number > value.number){
			//Agrega a la izquierda
			//verifico si la izquierda esta vacia
				if(!current.left){
					current.left = newNode;
					return true;
				}else{
                    //Si la izquierda no esta vacia
                    //Entonces agrego el nuevo nodo
                    //tomamos en cuenta que el nodo actual
                    //que es el nodo izquierdo es mi nuevo root
                    return this.add(value, current.left);
				}

            }

            else if(current.value.number < value.number){
				if(!current.right){
					current.right = newNode;
					return true;
                }
                else{
					return this.add(value,current.right);
				}
			}
		}
		return false;
    }

	function BSTDeleteContact(number, node=this.root){
		if(number == node.number){
			left = node.left
			node = node.right
			this.add(left,node)
		}
		else{
			parent = this.search(number)
			if(parent.right.number == number){
				left = parent.right.left
				parent.right = parent.right.right
				this.add(left,parent.right)
				return true
			}
			else if(parent.left.number == number){
				left = parent.left.left
				parent.left = parent.left.right
				this.add(left,parent.left)
				return true
			}
		}
		return false
	}

    function BSTSearch(number, parentNode = this.root){
        if(!this.root){
            return null;
        }
    
        else{
            if(parentNode.value.number == number){
                return parentNode;
            }
    
            else if(parentNode.value.number > number){
                if(parentNode.left){
                    return this.search(number, parentNode.left);
                }
                else{
                    return null;
                }
            }
    
            else{
                if(parentNode.right){
                    return this.search(number, parent.right);
                }
                else{
                    return null;
                }
            }
        }
    }
        

		function BSTPrint(current = this.root){
			if(current){
                if(current.left){
                    this.print(current.left);
                }
                console.log(current.value.name + ": " + current.value.number);

                if(current.right){
                    this.print(current.right);
                }
			}
		}