#                        ***************Nodo***************
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#                            *****Arbol Binario******
class BST:
    def __init__(self):
        
        self.root = None

    def BSTSearch(self,value, typeOfValue):
            if(typeOfValue == "number"):
                return self.searchNumerically(value,self.root)
            
            else:
                return self.searchAlphabetically(value,self.root)
            


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
                    return True
                
            
            else:
                if(current.right):
                    return self.addInnerNumerically(newNode,current.right)
                
                else:
                    current.right = newNode
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
    
    def BSTDeleteNumerically(self,value, current):
        if(not self.root):
            return False
        
        elif(self.searchNumerically(value,current)):
            return False
        
        else:
            if(self.root.value.number == value):
                leftChildren = self.root.left
                rightChildren = self.root.right

                self.root = None

                if(rightChildren):
                    self.addNumerically(rightChildren)
                
                if(leftChildren):
                    self.addNumerically(leftChildren)
                
                return True
            

            elif(current.value.number > value):
                if(current.left):
                    if(current.left.value.number == value):
                        leftChildren = current.left
                        rightChildren = current.right

                        current.left = None

                        if(rightChildren):
                            self.addNumerically(rightChildren)
                        
                        if(leftChildren):
                            self.addNumerically(leftChildren)
                        
                        return True
                    
                    else:
                        return self.BSTDeleteNumerically(value, current.left)
             
            else:
                if(current.value.number > value):
                    if(current.right):
                        if(current.right.value.number == value):
                            leftChildren = current.left
                            rightChildren = current.right

                            current.right = None

                            if(rightChildren):
                                self.addNumerically(rightChildren)
                            
                            if(leftChildren):
                                self.addNumerically(leftChildren)
                            
                            return True
                        
                        else:
                            return self.BSTDeleteNumerically(value, current.right)
    
    
    
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
            return True
        
        else:
            if(current.searchvalue.name == searchValue):
                return current
            
            elif(current.searchValue.name > searchValue):
                if(current.left):
                    return self.searchNumerically(searchValue, current.left)
                
                else:
                    return False
                
            else:
                if(current.right):
                    return self.searchNumerically(searchValue, current.right)
                
                else:
                    return False