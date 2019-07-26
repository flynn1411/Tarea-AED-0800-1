#                        ***************Nodo***************
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

        self.parent = None

#                            *****Arbol Binario******
class BST:
    def __init__(self):
        
        self.root = None

    def search(self,value, typeOfValue):
            if(typeOfValue == "number"):
                return self.searchNumerically(value,self.root)
            
            else:
                return self.searchAlphabetically(value,self.root)

    def _print(self):
        return self._printInner(self.root)

    def _printInner(self, current, trail = ""):
        if(current):
            trail += ("%s%s: %s \n %s" %(self._printInner(current.left, trail), current.value.name, current.value.number, self._printInner(current.right, trail)))
        return trail
            


#                            *****Arbol Binario por Numero******



    def addNumerically(self,newNode):

        return self.addInnerNumerically(newNode,self.root)
    
    
    def addInnerNumerically(self,newNode, current):
        if(not self.root):
            self.root = newNode
            return True
        
        else:
            if(current.value.number > newNode.value.number):
                if(current.left):
                    return self.addInnerNumerically(newNode,current.left)
                
                else:
                    current.left = newNode
                    current.left.parent = current
                    return True
                
            
            else:
                if(current.right):
                    return self.addInnerNumerically(newNode,current.right)
                
                else:
                    current.right = newNode
                    current.right.parent = current
                    return True
                   
        return False
    
    
      
    def searchNumerically(self,searchValue,current):
        if(not self.root):
            return True
        
        else:
            if(current.searchvalue.number == searchValue):
                return current
            
            elif(current.searchValue.number > searchValue):
                if(current.left):
                    return self.searchNumerically(searchValue, current.left)
                
                else:
                    return False
                
            else:
                if(current.right):
                    return self.searchNumerically(searchValue, current.right)
                
                else:
                    return False
    
    def deleteNumerically(self,deleteValue):
        if(deleteValue is self.root.value.number):
            left = self.root.left
            right = self.root.right
            self.root = None
            if(right):
                self.addNumerically(right)

            if(left):
                self.addNumerically(left)

            return True
        else:
            parent = self.searchNumerically(deleteValue, self.root).parent
            if(parent.right):
                if(parent.right.value.number is deleteValue):
                    left = parent.right.left
                    right = parent.right.right
                    parent.right = None
                    
                    if(right):
                        self.addNumerically(right)
        
                    if(left):
                        self.addNumerically(left)
        
                    return True
    

            elif(parent.left):
                if(parent.left.value.number is deleteValue):
                    left = parent.left.left
                    right = parent.left.right
                    parent.left = None
                    if(right):
                        self.addNumerically(right)
        
                    if(left):
                        self.addNumerically(left)
        
                    return True
    
        return False
    
    
    
#                            *****Arbol Binario por Nombre******

  
    
    def addAlphabetically(self,newNode):

        return self.addInnerAlphabetically(newNode,self.root)
    
    
    def addInnerAlphabetically(self,newNode, current):
        if(not self.root):
            self.root = newNode
            return True
        
        else:
            if(current.value.name > newNode.value.name):
                if(current.left):
                    return self.addInnerAlphabetically(newNode,current.left)
                
                else:
                    current.left = newNode
                    return True
                
            
            else:
                if(current.right):
                    return self.addInnerAlphabetically(newNode,current.right)
                
                else:
                    current.right = newNode
                    return True
                   
        return False

    def searchAlphabetically(self,searchValue,current):
        if(not self.root):
            return None
        
        else:
            if(current.searchvalue.name == searchValue):
                return current
            
            elif(current.searchValue.name > searchValue):
                if(current.left):
                    return self.searchNumerically(searchValue, current.left)
                
                else:
                    return None
                
            else:
                if(current.right):
                    return self.searchNumerically(searchValue, current.right)
                
                else:
                    return None

    def deleteAlphabetically(self,deleteValue):
        if(deleteValue is self.root.value.name):
            left = self.root.left
            right = self.root.right
            self.root = None
            if(right):
                self.addNumerically(right)

            if(left):
                self.addNumerically(left)

            return True
        else:
            parent = self.searchNumerically(deleteValue, self.root).parent
            if(parent.right):
                if(parent.right.value.name is deleteValue):
                    left = parent.right.left
                    right = parent.right.right
                    parent.right = None
                    
                    if(right):
                        self.addNumerically(right)
        
                    if(left):
                        self.addNumerically(left)
        
                    return True
    

            elif(parent.left):
                if(parent.left.value.name is deleteValue):
                    left = parent.left.left
                    right = parent.left.right
                    parent.left = None
                    if(right):
                        self.addNumerically(right)
        
                    if(left):
                        self.addNumerically(left)
        
                    return True
    
        return False
    