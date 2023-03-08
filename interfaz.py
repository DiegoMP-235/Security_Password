from tkinter import *
from Password import *



    
    
    
ventana = Tk()
ventana.title("Contraseña Segura")
ventana.geometry("400x320")

#instanciamos objeto de mi password
myPassword = Password()

#Definimos funciones
def generaPassword():
    Longitud = EntradaLen.getint()
    CaracteresEspeciales = CaracteresEspecialesBtn.getboolean()
    Mayusculas = MayusculasBtn.getboolean()
    Numeros = NumerosBtn.getboolean()
   
    print(CaracteresEspeciales,Mayusculas,Numeros)
    """ 
    myPassword.setCaracteresEsp(CaracteresEspeciales)
    myPassword.setMayusculas(Mayusculas)
    myPassword.setNumeros(Numeros)
    """

FrameControlsPass = Frame(ventana,bg="#00FF00")
FrameControlsPass.pack(expand=True,fill="both")

FrameBtn = Frame(ventana,bg="#FF0000")
FrameBtn.pack(expand=True,fill="both")

EtiquetaLen = Label(FrameControlsPass,text="Longitud:")
EtiquetaLen.pack()

EntradaLen = Entry(FrameControlsPass)
EntradaLen.pack()
#Caracteres especiales
EtiquetaCE = Label(FrameControlsPass,text="Caracteres Especiales")
EtiquetaCE.pack()

CaracteresEspecialesBtn = Checkbutton(FrameControlsPass)
CaracteresEspecialesBtn.pack()

#Mayusculas
EtiquetaMA = Label(FrameControlsPass,text="Mayusculas")
EtiquetaMA.pack()

MayusculasBtn = Checkbutton(FrameControlsPass)
MayusculasBtn.pack()

#Numeros
EtiquetaNum = Label(FrameControlsPass,text="Numeros")
EtiquetaNum.pack()

NumerosBtn = Checkbutton(FrameControlsPass)
NumerosBtn.pack()

#Controles
BtnGenerar=Button(FrameBtn,text="Generar",command=generaPassword)
BtnGenerar.pack()

SalidaPass = Entry(FrameBtn)
SalidaPass.pack()

myPassword.generaPassword()
print(myPassword.getPassword())

ventana.mainloop()