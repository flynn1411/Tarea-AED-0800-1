function BSTSearchContact()

actual = this.root;
parent = null;

parent = actual;
actual = actual.left;



function BSTDeleteContact(number, parentNode = null, current = this.root){
    if(this.search(number)){
        if(!this.root){
            return "No hay contactos";
        }

        else{
            //si se quiere borrar la raiz
            if(this.root.value.number == number){
                var leftChildren = this.root.left;
                var rightChildren = this.root.right;

                this.root = null;

                if(rightChildren){
                    this.add(rightChildren);
                }

                if(leftChildren){
                    this.add(rightChildren);
                }
                return true;
            }

            else if(current.value.number > number){
                if(current.left.value.number == number){
                    leftChildren = current.left.left;
                    rightChildren = current.left.right;

                    current.left = null;

                    if(rightChildren){
                        this.add(rightChildren);
                    }
    
                    if(leftChildren){
                        this.add(rightChildren);
                    }

                    return true;
                }
                else{
                    return this.delete(number, current, current.left);
                }
            }

            else{
                if(current.right.value.number == number){
                    leftChildren = current.right.left;
                    rightChildren = current.right.right;

                    current.right = null;

                    if(rightChildren){
                        this.add(rightChildren);
                    }
    
                    if(leftChildren){
                        this.add(rightChildren);
                    }

                    return true;
                }
                else{
                    return this.delete(number, current, current.right);
                }
            }
        }
    }
    else{
        return `El número ${numero} no existe.`;
    }
    
}