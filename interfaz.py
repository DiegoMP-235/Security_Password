from tkinter import Tk,messagebox,Entry,Frame,Label,Checkbutton,Button,BooleanVar
from Password import *


ventana = Tk()
ventana.title("Contraseña Segura")
ventana.geometry("400x320")

#instanciamos objeto de mi password
myPassword = Password()
#Definimos las variables para los checkbutton
EncenCaracEsp = BooleanVar()
EncenMayusculas = BooleanVar()
EncNumeros = BooleanVar()

#Definimos funciones
def generaPassword():
    myPassword.setLongitud(int(EntradaLen.get()))
    myPassword.setCaracteresEsp(EncenCaracEsp.get())
    myPassword.setMayusculas(EncenMayusculas.get())
    myPassword.setNumeros(EncNumeros.get())
    myPassword.crearPassword()
    nuevaPass = myPassword.getPassword()
    messagebox.showinfo("Esta es tu clave",nuevaPass)


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

CaracteresEspecialesBtn = Checkbutton(FrameControlsPass,variable=EncenCaracEsp)
CaracteresEspecialesBtn.pack()

#Mayusculas
EtiquetaMA = Label(FrameControlsPass,text="Mayusculas")
EtiquetaMA.pack()

MayusculasBtn = Checkbutton(FrameControlsPass,variable=EncenMayusculas)
MayusculasBtn.pack()

#Numeros
EtiquetaNum = Label(FrameControlsPass,text="Numeros")
EtiquetaNum.pack()

NumerosBtn = Checkbutton(FrameControlsPass,variable=EncNumeros)
NumerosBtn.pack()

#Controles
BtnGenerar=Button(FrameBtn,text="Generar",command=generaPassword)
BtnGenerar.pack()

SalidaPass = Entry(FrameBtn)
SalidaPass.pack()
ventana.mainloop()