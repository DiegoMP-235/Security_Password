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
      
    """
            
    def getCaracteresHabilitados(self): #esta podria ser una solucion muy estatica, pero por el momento es para salir del apuro        
        totalCaracteres = 1 #en caso de que se mantenga en 1 solo generara en base a las minusculas
        if(self.__CaracteresEsp == True):
            totalCaracteres = totalCaracteres+1
            
        if(self.__Mayusculas == True):
            totalCaracteres = totalCaracteres+1  
        
        if(self.__Numeros == True):
            totalCaracteres = totalCaracteres+1 
      """      
    
    def __getCaracteresEsp(self):
        return self.__CaracteresEsp
    
    def __getMayusculas(self):
        return self.__Mayusculas
    
    def __getNumeros(self):
        return self.__Numeros
    
    def generaPassword(self):   
        Password = ""  
        Caracteres = ["abcdefghijklmnopqrstuvwxyz","ÑñÁáÍí[]{/}","ABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789"]      
        #Obtiene de que conjunto habilitado obtendra el caracter
              
        for i in range(1,self.__longitud):
            Conjunto = random.randint(0,len(Caracteres)-1)
            Password = Password + Caracteres[Conjunto][random.randint(0,len(Conjunto)-1)]
            