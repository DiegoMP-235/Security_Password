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
    SalidaPass.delete(0,'end')
    SalidaPass.insert(0,nuevaPass)


FrameControlsPass = Frame(ventana,bg="#00FF00")
FrameControlsPass.pack(expand=True,fill="both")

FrameBtn = Frame(ventana,bg="#FF0000")
FrameBtn.pack(expand=True,fill="both")

EtiquetaLen = Label(FrameControlsPass,text="Longitud:")
EtiquetaLen.pack()

EntradaLen = Entry(FrameControlsPass)
EntradaLen.pack()
#Caracteres especiales
CaracteresEspecialesBtn = Checkbutton(FrameControlsPass,text="Caracteres especiales",variable=EncenCaracEsp)
CaracteresEspecialesBtn.pack()

#Mayusculas
MayusculasBtn = Checkbutton(FrameControlsPass,text="Mayusculas",variable=EncenMayusculas)
MayusculasBtn.pack()

#Numeros
NumerosBtn = Checkbutton(FrameControlsPass,text="Numeros",variable=EncNumeros)
NumerosBtn.pack()

#Controles
BtnGenerar=Button(FrameBtn,text="Generar",command=generaPassword)
BtnGenerar.pack()

SalidaPass = Entry(FrameBtn)
SalidaPass.pack()

#About Fortaleza
LabFortaleza = Label(FrameBtn,text="Fortaleza:")
LabFortaleza.pack()

#Seteamos la longitud por defecto en el Entry
EntradaLen.insert(0,myPassword.getLongitud())

ventana.mainloop()