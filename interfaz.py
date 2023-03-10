from tkinter import Tk,messagebox,Entry,Frame,Label,Checkbutton,Button,BooleanVar
from Password import *
from Validaciones import *

ventana = Tk()
ventana.title("Contraseña Segura")
ventana.geometry("400x320")
ventana.minsize(280,200)
ventana.maxsize(400,320)

#instanciamos objeto de mi password
myPassword = Password()
#instanciamos objeto de validaciones
Validar = Validaciones()
#Definimos las variables para los checkbutton
EncenCaracEsp = BooleanVar()
EncenMayusculas = BooleanVar()
EncNumeros = BooleanVar()


#Definimos funciones
def muestraPassword():
    nuevaPass = myPassword.getPassword()
    messagebox.showinfo("Esta es tu clave",nuevaPass)
    SalidaPass.delete(0,'end')
    SalidaPass.insert(0,nuevaPass)
    LabFortaleza.config(text=myPassword.getFortaleza())
    
def generaPassword():

    if(Validar.camposVacios(EntradaLen.get())):
        messagebox.showinfo("Campleta campos","Por favor completa los campos")
    else:
        if(not Validar.esNumero(EntradaLen.get())): 
            messagebox.showerror("Solo numeros","FATAL ERROR! ⚠️🚨\nUN ROOTKIT ENCONTRADO (ಥ﹏ಥ)")
        else:      
            myPassword.setLongitud(int(EntradaLen.get()))
            myPassword.setCaracteresEsp(EncenCaracEsp.get())
            myPassword.setMayusculas(EncenMayusculas.get())
            myPassword.setNumeros(EncNumeros.get())
            myPassword.crearPassword()
            muestraPassword()


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
SeccionFrotaleza = Frame(FrameBtn)

LblIndFort = Label(SeccionFrotaleza,text="Nivel de fortaleza:")
LblIndFort.grid(row=0,column=0)

LabFortaleza = Label(SeccionFrotaleza,text="[Fortaleza]")
LabFortaleza.grid(row=0,column=1)

SeccionFrotaleza.pack()

#Seteamos la longitud por defecto en el Entry
EntradaLen.insert(0,myPassword.getLongitud())
LabFortaleza.config(text=myPassword.getFortaleza())

ventana.mainloop()