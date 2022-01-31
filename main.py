from tkinter import *


def km_to_miles():
    km=float(Entrada_km.get())
    millas=str(round(km/1.60934,2))
    MillasC_label.config(text=f"{millas}")

ventana = Tk()
ventana.title("Conversor KM a Millas Python TK")
ventana.config(padx=20,pady=20)

Entrada_km = Entry(width=7)
Entrada_km.grid(column=1,row=0)


Km_label = Label(text="Km")
Km_label.grid(column=2,row=0)

es_igual_etiqueta = Label(text="es igual a")
es_igual_etiqueta.grid(column=0,row=1)


MillasC_label = Label(text="-")
MillasC_label.grid(column=1,row=1)

Millas_label = Label(text="Millas")
Millas_label.grid(column=2,row=1)

boton_calcular = Button(text="Calcular", command=km_to_miles)
boton_calcular.grid(column=1,row=2)























ventana.mainloop()