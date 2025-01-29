from tkinter import *
#comentario de prueba

# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
ancho = 1020
alto = 630
aplicacion.geometry(f"{ancho}x{alto}+0+0")

# Evitar maximizar ventana
aplicacion.resizable(False, False)

# Título de la ventana
aplicacion.title("Calculadora de Administración Financiera")

# Colores paleta coffee:
blanco = "FFFFFF"
cafe_claro = "F9E0BB"
amarillo = "FFC26F"
cafe_medio = "C38154"
cafe_oscuro = "8B5A2B"
negro = "000000"

# Color fondo ventana
aplicacion.config(bg=f"#{cafe_claro}")

# Menú lateral
menu_lateral = Frame(aplicacion, bg=f"#{cafe_oscuro}", width=200, height=alto)
menu_lateral.pack(side="left", fill="y")

# Área principal
area_principal = Frame(aplicacion, bg=f"#{cafe_claro}", width=ancho - 200, height=alto)
area_principal.pack(side="right", fill="both", expand=True)


# Crea paneles de título y descripción para usar en cada sección
def paneles_comunes(titulo, descripcion):
    # Panel superior
    panel_superior = Frame(area_principal, relief=FLAT, bg=f"#{cafe_claro}")
    panel_superior.pack(side=TOP)

    #Título
    etiqueta_titulo = Label(panel_superior, text=titulo, fg=f"#{cafe_oscuro}",
                            font=("Dosis", 16), bg=f"#{cafe_claro}", width=0)
    etiqueta_titulo.pack(pady=40)

    # Panel descripción
    panel_descripcion = Frame(area_principal, relief=FLAT, bg=f"#{cafe_claro}")
    panel_descripcion.pack(side=TOP)

    # Descripción
    etiqueta_descripcion = Label(panel_descripcion, text=descripcion, fg=f"#{cafe_medio}",
                                 font=("Dosis", 12), bg=f"#{cafe_claro}", width=0,
                                 wraplength=ancho - 120, justify="left")
    etiqueta_descripcion.pack(pady=0)

    # Retorna los paneles comunes
    return panel_superior, panel_descripcion


def limpiar_area_principal():
    for widget in area_principal.winfo_children():
        widget.destroy()


def mostrar_ingresos():
    limpiar_area_principal()
    titulo_ingresos = "Ingresos mensuales"
    descripcion_ingresos = ('Seleccione las casillas de los ingresos que usted reciba mensualmente e ingrese los '
                            'valores correspondientes. Puede añadir otros campos con el botón "Agregar", asegúrese '
                            'de clickear la casilla, escribir un nombre y el valor.')
    paneles_comunes(titulo_ingresos, descripcion_ingresos)



def mostrar_gastos():
    limpiar_area_principal()
    titulo_gastos = "Gastos mensuales"
    descripcion_gastos = ('Seleccione las casillas de los gastos que usted efectúa mensualmente e ingrese los '
                            'valores correspondientes. Puede añadir otros campos con el botón "Agregar", asegúrese '
                            'de clickear la casilla, escribir un nombre y el valor.')
    paneles_comunes(titulo_gastos, descripcion_gastos)


def mostrar_resultados():
    limpiar_area_principal()
    titulo_resultados = "Resultados"
    descripcion_resultados = ('Es recomendable que se administre económicamente así:')
    paneles_comunes(titulo_resultados, descripcion_resultados)


def mostrar_inicio():
    limpiar_area_principal()
    titulo_inicio = "Ingresos mensuales"
    descripcion_inicio = ('Seleccione las casillas de los ingresos que usted reciba mensualmente e ingrese los '
                            'valores correspondientes. Puede añadir otros campos con el botón "Agregar", asegúrese '
                            'de clickear la casilla, escribir un nombre y el valor.')
    paneles_comunes(titulo_inicio, descripcion_inicio)


# Botones del menú lateral
boton_inicio = Button(menu_lateral, text="Inicio", bg=f"#{cafe_claro}", fg="black", font=("Arial", 12),
                          relief="raised", command=mostrar_inicio)
boton_inicio.pack(pady=10, padx=10, fill="x")

boton_ingresos = Button(menu_lateral, text="Ingresos", bg=f"#{cafe_claro}", fg="black", font=("Arial", 12),
                        relief="raised", command=mostrar_ingresos)
boton_ingresos.pack(pady=10, padx=10, fill="x")

boton_gastos = Button(menu_lateral, text="Gastos", bg=f"#{cafe_claro}", fg="black", font=("Arial", 12), relief="raised",
                      command=mostrar_gastos)
boton_gastos.pack(pady=10, padx=10, fill="x")

boton_resultados = Button(menu_lateral, text="Resultados", bg=f"#{cafe_claro}", fg="black", font=("Arial", 12),
                          relief="raised", command=mostrar_resultados)
boton_resultados.pack(pady=10, padx=10, fill="x")







# Llama a la función de inicio al inicio
mostrar_inicio()

# Lanza la aplicación
aplicacion.mainloop()

