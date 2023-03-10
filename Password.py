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
    def getFortaleza(self):
        return self.__fortaleza
    
    def crearPassword(self):   
        Password = ""  
        Caracteres = self.__getConjuntos()     
              
        for i in range(0,self.__longitud):
            Conjunto = random.randint(0,len(Caracteres)-1)
            Password = Password + Caracteres[Conjunto][random.randint(0,len(Caracteres[Conjunto])-1)]
        
        self.__setPassword(Password) 
        self.__setFortaleza(self.__determinaNivFort(self.__determinaPuntosFortaleza()))  
        #determinarfort
        
    def __determinaPuntosFortaleza(self):
         #print("determinando fortaleza...")
         puntosFort = 1
         if(self.getLongitud() >= 8):
             puntosFort += 3
             if(self.getLongitud() % 2 ==0 and self.getLongitud()>12):
                puntosFort+=2 
         if(self.getCaracteresEsp()):
             puntosFort += 3 
         if(self.getMayusculas()):
             puntosFort += 1
         if(self.getNumeros()): 
             puntosFort += 1           
         return puntosFort   
     
    def __determinaNivFort(self,puntosFort):
        NivelFort = "Calculando..."
        if(puntosFort >= 1 and puntosFort <= 4):
            NivelFort = "Mala"
        elif(puntosFort >= 5 and puntosFort <= 7):
            NivelFort = "Regular"    
        elif(puntosFort >= 8 and puntosFort <= 10): 
            NivelFort = "Buena"
        elif(puntosFort > 10):
            NivelFort = "Muy buena"     
        return NivelFort    
            
    def __setFortaleza(self,Fortaleza):
        self.__fortaleza = Fortaleza                  