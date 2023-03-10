from tkinter import Tk,messagebox,Entry,Frame,Label,Checkbutton,Button,BooleanVar
from Password import *

ventana = Tk()
ventana.title("Contraseña Segura")
ventana.geometry("400x320")
ventana.minsize(280,200)
ventana.maxsize(400,320)

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
    LabFortaleza.config(text=myPassword.getFortaleza())

FrameControlsPass = Frame(ventana,bg="#95a3a3")
FrameControlsPass.pack(expand=True,fill="both")

FrameBtn = Frame(ventana,bg="#95b5b6")
FrameBtn.pack(expand=True,fill="both")

LabelTittle = Label(FrameControlsPass,text="Contraseña segura",font=("Arial", 15, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle.pack()

EtiquetaLen = Label(FrameControlsPass,text="Longitud:")
EtiquetaLen.pack(pady=5)

EntradaLen = Entry(FrameControlsPass)
EntradaLen.pack()
#Caracteres especiales
CaracteresEspecialesBtn = Checkbutton(FrameControlsPass,text="Caracteres especiales",variable=EncenCaracEsp)
CaracteresEspecialesBtn.pack(pady=5)

#Mayusculas
MayusculasBtn = Checkbutton(FrameControlsPass,text="Mayusculas",variable=EncenMayusculas)
MayusculasBtn.pack(pady=5)

#Numeros
NumerosBtn = Checkbutton(FrameControlsPass,text="Numeros",variable=EncNumeros)
NumerosBtn.pack(pady=5)

#Controles
BtnGenerar=Button(FrameBtn,text="Generar",command=generaPassword)
BtnGenerar.pack(pady=5)

SalidaPass = Entry(FrameBtn)
SalidaPass.pack(pady=5)

#About Fortaleza
LabFortaleza = Label(FrameBtn,text="Fortaleza:")
LabFortaleza.pack(pady=5)

#Seteamos la longitud por defecto en el Entry
EntradaLen.insert(0,myPassword.getLongitud())
LabFortaleza.config(text=myPassword.getFortaleza())

ventana.mainloop()