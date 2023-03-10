class Validaciones:
    def __init__(self) -> None:
        self.__activo = True
    
    def camposVacios(self,Valor):
        if(Valor == ""):
            return True
        else:
            return False
    
    def esNumero(self,Value):
        esNumero = False
        for i in range(0,len(Value)):
            if(ord(Value[i]) < 47 or ord(Value[i]) > 58 ):
                return esNumero
            
        return not esNumero    