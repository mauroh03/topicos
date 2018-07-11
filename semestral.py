import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd
from matplotlib import interactive
from tkinter import *
from tkinter import ttk

def cargar():
    global df
    global fullDf
    fullDf = pd.read_csv('./resumen_mes.csv')
    df = pd.read_csv('./resumen_mes.csv', index_col="Fecha")
    label1 = Label(ventana, text="CSV cargado...", fg="green").place(relx=.105, rely=.15, anchor="center")

    # col1
    col1 = ttk.Combobox(ventana, textvariable=strCol1)
    col1.place(relx=.225, rely=.330, anchor="center")
    col1['values']=(list(df))
    col1.current(0)
    # col2
    col2 = ttk.Combobox(ventana, textvariable=strCol2)
    col2['values']=(list(df))
    col2.place(relx=.425, rely=.330, anchor="center")
    col2.current(0)
    # col3
    col3 = ttk.Combobox(ventana, textvariable=strCol3)
    col3.place(relx=.625, rely=.330, anchor="center")
    col3['values']=(list(df))
    col3.current(0)
    # col4
    col4 = ttk.Combobox(ventana, textvariable=strCol4)
    col4.place(relx=.825, rely=.330, anchor="center")
    col4['values']=(list(df))
    col4.current(0)

def grafica():
    if strGraphType.get() == 'Puntos':
        plt.figure(1)
        plt.scatter(indexDf['Fecha'],indexDf[strFieldToGraph.get()])
        plt.ylabel(strFieldToGraph.get())
        plt.title('Grafico de '+strFieldToGraph.get())
        interactive(True)
    elif strGraphType.get() == 'Barras':
        plt.figure(2)
        plt.bar(indexDf['Fecha'],indexDf[strFieldToGraph.get()])
        plt.ylabel(strFieldToGraph.get())
        plt.title('Grafico de '+strFieldToGraph.get())
        interactive(True)
    else:
        plt.figure(2)
        plt.plot(indexDf['Fecha'],indexDf[strFieldToGraph.get()])
        plt.ylabel(strFieldToGraph.get())
        plt.title('Grafico de '+strFieldToGraph.get())
        interactive(True)

    plt.xticks(rotation=90)
    plt.xlabel('Fecha')
    plt.show()

def insertar():
    global filteredDf
    global indexDf
    global columns
    columns = [strCol1.get(), strCol2.get(), strCol3.get(), strCol4.get()]

    fieldToGraph = ttk.Combobox(ventana, textvariable=strFieldToGraph)
    fieldToGraph.place(relx=.625, rely=.245, anchor="center")
    fieldToGraph['values']=(columns)
    fieldToGraph.current(0)
    botonGraph = Button(ventana, text ="graficar", command=grafica).place(relx=.75, rely=.245, anchor="center")

    text = Text(ventana,width=120,height=23)
    text.insert(INSERT, "Fecha\t\t\t"+strCol1.get()+"\t\t\t"+strCol2.get()+"\t\t\t"+strCol3.get()+"\t\t\t"+strCol4.get()+"\n")
    text.place(relx=.5, rely=.65, anchor="center")
    if len(dia1.get()) > 1:
        strDia1 = dia1.get()
    else:
        strDia1 = '0'+dia1.get()
    if len(dia2.get()) > 1:
        strDia2 = dia2.get()
    else:
        strDia2 = '0'+dia2.get()
    filteredDf = df['2018-0'+mes1.get()+'-'+strDia1:'2018-0'+mes2.get()+'-'+strDia2]
    indexDf = filteredDf
    indexDf['Fecha'] = filteredDf.index.values
    indexDf.index=range(filteredDf.shape[0])
    indexDf.index += 1
    for x in range(filteredDf.shape[0]):
        m, s = divmod(int(indexDf.loc[x+1,'Dormir_duracion(ms)'])/1000, 60)
        h, m = divmod(m, 60)
        if strCol1.get() == 'Dormir_duracion(ms)':
            text.insert(INSERT, "%s\t\t\t%d:%02d:%02d\t\t\t%.2f\t\t\t%.2f\t\t\t%.2f\n" %(str(indexDf.loc[x+1,'Fecha']), h,m,s, float(indexDf.loc[x+1,strCol2.get()]),
                        float(indexDf.loc[x+1,strCol3.get()]), float(indexDf.loc[x+1,strCol4.get()])))
        elif strCol2.get() == 'Dormir_duracion(ms)':
            text.insert(INSERT, "%s\t\t\t%.2f\t\t\t%d:%02d:%02d\t\t\t%.2f\t\t\t%.2f\n" %(str(indexDf.loc[x+1,'Fecha']), float(indexDf.loc[x+1,strCol1.get()]),
                        h,m,s, float(indexDf.loc[x+1,strCol3.get()]), float(indexDf.loc[x+1,strCol4.get()])))
        elif strCol3.get() == 'Dormir_duracion(ms)':
            text.insert(INSERT, "%s\t\t\t%.2f\t\t\t%.2f\t\t\t%d:%02d:%02d\t\t\t%.2f\n" %(str(indexDf.loc[x+1,'Fecha']), float(indexDf.loc[x+1,strCol1.get()]),
                        float(indexDf.loc[x+1,strCol2.get()]), h,m,s, float(indexDf.loc[x+1,strCol4.get()])))
        elif strCol4.get() == 'Dormir_duracion(ms)':
            text.insert(INSERT, "%s\t\t\t%.2f\t\t\t%.2f\t\t\t%.2f\t\t\t%d:%02d:%02d\n" %(str(indexDf.loc[x+1,'Fecha']), float(indexDf.loc[x+1,strCol1.get()]),
                        float(indexDf.loc[x+1,strCol2.get()]), float(indexDf.loc[x+1,strCol3.get()]), h,m,s))
        else:
            text.insert(INSERT, "%s\t\t\t%.2f\t\t\t%.2f\t\t\t%.2f\t\t\t%.2f\n" %(str(indexDf.loc[x+1,'Fecha']), float(indexDf.loc[x+1,strCol1.get()]),
                        float(indexDf.loc[x+1,strCol2.get()]), float(indexDf.loc[x+1,strCol3.get()]),float(indexDf.loc[x+1,strCol4.get()])))

ventana = Tk()
ventana.title("Main Window")
ventana.geometry("1000x650")

strCol1=StringVar()
strCol2=StringVar()
strCol3=StringVar()
strCol4=StringVar()
strGraphType=StringVar()
strFieldToGraph=StringVar()

label1 = Label(ventana, text="carga de CSV...").place(relx=.105, rely=.15, anchor="center")
boton = Button(ventana, text ="cargar CSV", command=cargar).place(relx=.102, rely=.1, anchor="center")
botonFiltered = Button(ventana, text ="Insertar datos", command=insertar).place(relx=.25, rely=.2, anchor="center")

monthLabel1 = Label(ventana, text="mes: ").place(relx=.11, rely=.2, anchor="center")
mes1 = ttk.Combobox(ventana, width=2)
mes1.place(relx=.145, rely=.2, anchor="center")
mes1['values']=('4', '5', '6')
mes1.current(0)

dayLabel1 = Label(ventana, text="dia: ").place(relx=.033, rely=.2, anchor="center")
dia1 = ttk.Combobox(ventana, width=2)
dia1.place(relx=.067, rely=.2, anchor="center")
dia1['values']=(list(range(1,31)))
dia1.current(0)

monthLabel2 = Label(ventana, text="mes: ").place(relx=.11, rely=.245, anchor="center")
mes2 = ttk.Combobox(ventana, width=2)
mes2.place(relx=.145, rely=.245, anchor="center")
mes2['values']=('4', '5', '6')
mes2.current(0)

dayLabel2 = Label(ventana, text="dia: ").place(relx=.033, rely=.245, anchor="center")
dia2 = ttk.Combobox(ventana, width=2)
dia2.place(relx=.067, rely=.245, anchor="center")
dia2['values']=(list(range(1,31)))
dia2.current(0)

graphLabel = Label(ventana, text="tipo de grafica: ").place(relx=.490, rely=.2, anchor="center")
graphType = ttk.Combobox(ventana, textvariable=strGraphType)
graphType.place(relx=.604, rely=.2, anchor="center")
graphType['values']=('Puntos', 'Barras', 'Linea')
graphType.current(0)

fieldLabel = Label(ventana, text="columna a graficar: ").place(relx=.5, rely=.245, anchor="center")
ventana.mainloop()
