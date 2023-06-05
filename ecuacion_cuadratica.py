from tkinter import *
from tkinter import messagebox
from math import *
import cmath as mt


v = Tk()
v.title("Raices ecuación cuadratica")

Label(v, text= "Coeficiente A").grid(row=0, column=0)
Label(v, text= "Coeficiente B").grid(row=1, column=0)
Label(v, text= "Coeficiente C").grid(row=2, column=0)

Label(v, text= "Raiz X1").grid(row=4, column=0)
Label(v, text= "Raiz X2").grid(row=5, column=0)

txtA = Entry(v, width = 10)
txtA.grid(row=0, column = 1)
txtB = Entry(v, width = 10)
txtB.grid(row=1, column = 1)
txtC = Entry(v, width = 10)
txtC.grid(row=2, column = 1)

txtX1 = Entry(v, width = 40)
txtX1.grid(row=4, column = 1)
txtX2 = Entry(v, width = 40)
txtX2.grid(row=5, column = 1)

def calcularRaices():
    #Obtener datos de entrada
    a = float(txtA.get())
    b = float(txtB.get())
    c = float(txtC.get())

    #Proceso
    if a != 0:
        r = b**2-4*a*c
        if r > 0:
            x1 = (-b+sqrt(r))/(2*a)
            x2 = (-b-sqrt(r))/(2*a)
        else:
            x1 = (-b+mt.sqrt(r))/(2*a)
            x2 = (-b-mt.sqrt(r))/(2*a)
        txtX1.insert(0, str(x1))
        txtX2.insert(0, str(x2))
        
    else:
        messagebox.showerror("Error al calcular","La ecuación no es cuadratica")
        
      
Button(v, text= "Calcular", command=calcularRaices).grid(row =3, column = 0)

