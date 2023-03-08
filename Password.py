import random
class Password:
    def __init__(self):
        self.__password = ""
        self.__longitud = 8
        self.__CaracteresEsp = True 
        self.__Mayusculas = True
        self.__Numeros = True
        self.__fortalea = "No estabelcida"
        
    def setLongitud(self,Longitud):
        self.__longitud = Longitud
        
    def setCaracteresEsp(self,CaracteresEsp):
        if(self.__CaracteresEsp != True):
            self.__CaracteresEsp = True  
        else:
            self.__CaracteresEsp = False
            
    def setMayusculas(self,Mayusculas):
        if(self.__Mayusculas != True):
            self.__Mayusculas = True  
        else:
            self.__Mayusculas = False     
 
    def setNumeros(self,Numeros):
        if(self.__Numeros != True):
            self.__Numeros = True  
        else:
            self.__Mayusculas = False  
                          
    def getCaracteresEsp(self):
        return self.__CaracteresEsp
    
    def getMayusculas(self):
        return self.__Mayusculas
    
    def getNumeros(self):
        return self.__Numeros
    
    
    def getConjuntos(self):
        Caracteres = ["abcdefghijklmnopqrstuvwxyz"] 
        if(self.getCaracteresEsp() == True):   
            Caracteres.insert(len(Caracteres),"ÑñÁáÍí[]{/}")
            
        if(self.getMayusculas()  == True):
            Caracteres.insert(len(Caracteres),"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
        if(self.getNumeros()  == True):
            Caracteres.insert(len(Caracteres),"0123456789")
            
        return Caracteres    
    
    def setPassword(self,Password):
        self.__password = Password
        
    def getPassword(self):
        return self.__password
    
    def generaPassword(self):   
        Password = ""  
        Caracteres = self.getConjuntos()     
              
        for i in range(0,self.__longitud):
            Conjunto = random.randint(0,len(Caracteres)-1)
            Password = Password + Caracteres[Conjunto][random.randint(0,len(Caracteres[Conjunto])-1)]
        
        self.setPassword(Password)    
            
                                 