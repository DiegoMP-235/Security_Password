import random
class Password:
    def __init__(self):
        self.__password = ""
        self.__longitud = 8
        self.__CaracteresEsp = True 
        self.__Mayusculas = True
        self.__Numeros = True
        self.__CaracteresDefecto = "abcdefghijklmnopqrstuvwxyz"
        self.__ConjuntoCaracEsp = "!@#$%^+=~-_ÑñÁáÍí[]{/}"
        self.__ConjuntoMayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__ConjuntoNumeros = "0123456789"
        self.__fortaleza = "No estabelcida"
        
    def setLongitud(self,Longitud):
        self.__longitud = Longitud
        
    def setCaracteresEsp(self,CaracteresEsp):
        self.__CaracteresEsp = CaracteresEsp  

            
    def setMayusculas(self,Mayusculas):
        self.__Mayusculas = Mayusculas  
     
 
    def setNumeros(self,Numeros):
        self.__Numeros = Numeros  
  
    def getLongitud(self):
        return self.__longitud
                          
    def getCaracteresEsp(self):
        return self.__CaracteresEsp
    
    def getMayusculas(self):
        return self.__Mayusculas
    
    def getNumeros(self):
        return self.__Numeros
    
    
    def __getConjuntos(self):
        Caracteres = [self.__CaracteresDefecto] 
        if(self.getCaracteresEsp() == True):   
            Caracteres.insert(len(Caracteres),self.__ConjuntoCaracEsp)
            
        if(self.getMayusculas()  == True):
            Caracteres.insert(len(Caracteres),self.__ConjuntoMayusculas)
    
        if(self.getNumeros()  == True):
            Caracteres.insert(len(Caracteres),self.__ConjuntoNumeros)
            
        return Caracteres    
    
    def __setPassword(self,Password):
        self.__password = Password
        
    def getPassword(self):
        return self.__password
    
    def crearPassword(self):   
        Password = ""  
        Caracteres = self.__getConjuntos()     
              
        for i in range(0,self.__longitud):
            Conjunto = random.randint(0,len(Caracteres)-1)
            Password = Password + Caracteres[Conjunto][random.randint(0,len(Caracteres[Conjunto])-1)]
        
        self.__setPassword(Password)    
            
    def __setFortaleza(self):
        print("estableciendo Fortaleza..." )                         