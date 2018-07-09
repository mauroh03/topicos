import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import interactive
from tkinter import *
from tkinter import ttk

def cargar():
    global df
    df = pd.read_csv('./resumen_mes.csv', index_col="Fecha")
    label1 = Label(ventana, text="CSV cargado...", fg="green").place(relx=.5, rely=.05, anchor="center")

def prueba():
    print(df)

def filtro():
    global filteredDf
    filteredDf = df['2018-'+mes1.get()+'-'+dia1.get():'2018-'+mes2.get()+'-'+dia2.get()]
    print(filteredDf)

ventana = Tk()
ventana.title("Main Window")
ventana.geometry("800x600")

label1 = Label(ventana, text="carga de CSV...").place(relx=.5, rely=.05, anchor="center")
boton = Button(ventana, text ="cargar CSV", command=cargar).place(relx=.5, rely=.1, anchor="center")
botonTest = Button(ventana, text ="prueba", command=prueba).place(relx=.7, rely=.1, anchor="center")
botonFiltered = Button(ventana, text ="filtrado", command=filtro).place(relx=.3, rely=.1, anchor="center")

monthLabel1 = Label(ventana, text="mes: ").place(relx=.05, rely=.2, anchor="center")
mes1 = ttk.Combobox(ventana)
mes1.place(relx=.16, rely=.2, anchor="center")
mes1['values']=('4', '5', '6')
mes1.current(0)

dayLabel1 = Label(ventana, text="dia: ").place(relx=.05, rely=.3, anchor="center")
dia1 = ttk.Combobox(ventana)
dia1.place(relx=.16, rely=.3, anchor="center")
dia1['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30')
dia1.current(0)

monthLabel2 = Label(ventana, text="mes: ").place(relx=.4, rely=.2, anchor="center")
mes2 = ttk.Combobox(ventana)
mes2.place(relx=.56, rely=.2, anchor="center")
mes2['values']=('4', '5', '6')
mes2.current(0)

dayLabel2 = Label(ventana, text="dia: ").place(relx=.4, rely=.3, anchor="center")
dia2 = ttk.Combobox(ventana)
dia2.place(relx=.56, rely=.3, anchor="center")
dia2['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30')
dia2.current(0)

ventana.mainloop()
