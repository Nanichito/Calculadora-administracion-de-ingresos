from tkinter import *

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
menu_lateral = Frame(aplicacion,
                     bg=f"#{cafe_oscuro}",
                     width=200,
                     height=alto)
menu_lateral.pack(side="left",
                  fill="y")

# Área principal
area_principal = Frame(aplicacion,
                       bg=f"#{cafe_claro}",
                       width=ancho - 200,
                       height=alto)
area_principal.pack(side="right",
                    fill="both",
                    expand=True)

# Lista opciones ingresos
lista_ingresos = ["Sueldo líquido", "Otro 1", "Otro 2", "Otro 3", "Otro 4", "Otro 5", "Otro 6", "Otro 7"]



#Paneles comunes para todas las secciones
def paneles_comunes(titulo, descripcion):
    # Panel superior
    panel_superior = Frame(area_principal,
                           relief=FLAT,
                           bg=f"#{cafe_claro}")
    panel_superior.pack(side=TOP)

    #Título
    etiqueta_titulo = Label(panel_superior,
                            text=titulo,
                            fg=f"#{cafe_oscuro}",
                            font=("Dosis", 16),
                            bg=f"#{cafe_claro}",
                            width=0)
    etiqueta_titulo.pack(pady=40)

    # Panel descripción
    panel_descripcion = Frame(area_principal,
                              relief=FLAT,
                              bg=f"#{cafe_claro}")
    panel_descripcion.pack(side=TOP)

    # Descripción
    etiqueta_descripcion = Label(panel_descripcion,
                                 text=descripcion,
                                 fg=f"#{cafe_medio}",
                                 font=("Dosis", 12),
                                 bg=f"#{cafe_claro}",
                                 width=0,
                                 wraplength=ancho - 120,
                                 justify="left")
    etiqueta_descripcion.pack(pady=0)




    # Retorna los paneles comunes
    return panel_superior, panel_descripcion





# Elimina todos los widgets de la pantalla
def limpiar_area_principal():
    for widget in area_principal.winfo_children():
        widget.destroy()


# Funciones para cada sección
# Sección inicio
def mostrar_inicio():
    limpiar_area_principal()
    titulo_inicio = "Inicio"
    descripcion_inicio = ('Sigue las instrucciones de "Ingresos" y "Gastos" para obtener '
                          'una recomendación financiera en "Resultados')
    paneles_comunes(titulo_inicio, descripcion_inicio)






# Sección ingresos
def mostrar_ingresos():
    limpiar_area_principal()
    titulo_ingresos = "Ingresos mensuales"
    descripcion_ingresos = ('Seleccione las casillas de los ingresos que usted reciba mensualmente e ingrese los '
                            'valores correspondientes. Puede añadir otros campos con el botón "Agregar", asegúrese '
                            'de clickear la casilla, escribir un nombre y el valor.')
    paneles_comunes(titulo_ingresos, descripcion_ingresos)




    #Panel izquierdo
    panel_izquierdo = Frame(area_principal,
                            bd=1,
                            relief=FLAT,
                            bg=f"#{blanco}")
    panel_izquierdo.pack(side=LEFT)


    # Panel ingresos totales
    panel_ingresos_totales = Frame(panel_izquierdo,
                                   bd=1,
                                   relief=FLAT,
                                   bg=f"#{cafe_oscuro}",
                                   padx=120)
    panel_ingresos_totales.pack(side=BOTTOM)


    #Panel derecha
    panel_derecho = Frame(area_principal,
                          bd=1,
                          relief=FLAT,
                          bg=f"#{cafe_claro}")
    panel_derecho.pack(side=RIGHT)


    # Panel columna 1
    panel_columna1 = LabelFrame(panel_izquierdo,
                                text="Columna 1",
                                font=("Dosis", 15, "bold"),
                                bd=1,
                                relief=FLAT,
                                fg=f"#{cafe_oscuro}",
                                bg= f"#{blanco}")
    panel_columna1.pack(side=LEFT,
                        padx=(20, 0))

    # Panel columna 2
    panel_columna2 = LabelFrame(panel_izquierdo,
                                text="Columna 2",
                                font=("Dosis", 15, "bold"),
                                bd=1,
                                relief=FLAT,
                                fg=f"#{cafe_oscuro}",
                                bg= f"#{blanco}")
    panel_columna2.pack(side=LEFT,
                        padx=(30, 0))

    # Panel columna 3
    panel_columna3 = LabelFrame(panel_izquierdo,
                                text="Columna 3",
                                font=("Dosis", 15, "bold"),
                                bd=1,
                                relief=FLAT,
                                fg=f"#{cafe_oscuro}",
                                bg= f"#{blanco}")
    panel_columna3.pack(side=LEFT)





    # Generar items ingresos columna 1
    variables_ingresos1 = []
    cuadros_ingresos1 = []
    texto_ingresos1 = []


    # CheckButtons columna 1
    contador = 0
    for tipo_ingreso in lista_ingresos:
        variables_ingresos1.append("")
        variables_ingresos1[contador] = IntVar
        tipo_ingreso = Checkbutton(panel_columna1,
                                   text=tipo_ingreso.title(),
                                   font=("Dosis", 15, "italic"),
                                   fg=f"#{cafe_medio}",
                                   onvalue=1,
                                   offvalue=0,
                                   bg=f"#{blanco}",
                                   activebackground=f"#{cafe_claro}",
                                   variable=variables_ingresos1[contador])

        tipo_ingreso.grid(row=contador,
                          column=0,
                          sticky=W)

        # Crear los cuadros de entrada columna 1
        cuadros_ingresos1.append("")
        texto_ingresos1.append("")
        texto_ingresos1[contador] = StringVar()
        texto_ingresos1[contador].set("0")
        cuadros_ingresos1[contador] = Entry(panel_columna1,
                                           font=("Dosis", 15),
                                           bd=1,
                                           width=6,
                                           state=DISABLED,
                                           textvariable=texto_ingresos1[contador])
        cuadros_ingresos1[contador].grid(row=contador,
                                        column=1,
                                         padx=(8, 0))
        contador += 1



    # Generar items ingresos columna 2
    variables_ingresos2 = []
    cuadros_ingresos2 = []
    texto_ingresos2 = []

    # CheckButtons columna 2
    contador = 0
    for tipo_ingreso in lista_ingresos:
        variables_ingresos2.append("")
        variables_ingresos2[contador] = IntVar
        tipo_ingreso = Checkbutton(panel_columna2,
                                   text=tipo_ingreso.title(),
                                   font=("Dosis", 15, "italic"),
                                   fg=f"#{cafe_medio}",
                                   onvalue=1,
                                   offvalue=0,
                                   bg=f"#{blanco}",
                                   activebackground=f"#{cafe_claro}",
                                   variable=variables_ingresos2[contador])

        tipo_ingreso.grid(row=contador,
                          column=0,
                          sticky=W)

        # Crear los cuadros de entrada columna 2
        cuadros_ingresos2.append("")
        texto_ingresos2.append("")
        texto_ingresos2[contador] = StringVar()
        texto_ingresos2[contador].set("0")
        cuadros_ingresos2[contador] = Entry(panel_columna2,
                                            font=("Dosis", 15),
                                            bd=1,
                                            width=6,
                                            state=DISABLED,
                                            textvariable=texto_ingresos2[contador])
        cuadros_ingresos2[contador].grid(row=contador,
                                         column=1,
                                         padx=(8, 0))
        contador += 1


    # Variables ingresos totales
    var_ingresos_totales = StringVar()
    # Etiquetas de ingresos totales y campos de entrada
    etiqueta_ingresos_totales = Label(panel_ingresos_totales,
                                      text=("Ingresos mensuales totales"),
                                      font=("Dosis", 12),
                                      bg=f"#{cafe_oscuro}",
                                      fg=f"#{blanco}")
    etiqueta_ingresos_totales.grid(row=0,
                                   column=0)

    texto_ingresos_totales = Entry(panel_ingresos_totales,
                                   font=("Dosis", 12),
                                   bd=1,
                                   width=10,
                                   state="readonly",
                                   textvariable=var_ingresos_totales)
    texto_ingresos_totales.grid(row=0,
                                column=1,
                                padx=5)





# Sección gastos
def mostrar_gastos():
    limpiar_area_principal()
    titulo_gastos = "Gastos mensuales"
    descripcion_gastos = ('Seleccione las casillas de los gastos que usted efectúa mensualmente e ingrese los '
                            'valores correspondientes. Puede añadir otros campos con el botón "Agregar", asegúrese '
                            'de clickear la casilla, escribir un nombre y el valor.')
    paneles_comunes(titulo_gastos, descripcion_gastos)


# Sección resultados
def mostrar_resultados():
    limpiar_area_principal()
    titulo_resultados = "Resultados"
    descripcion_resultados = ('Es recomendable que se administre económicamente así:')
    paneles_comunes(titulo_resultados, descripcion_resultados)




# Botones del menú lateral
boton_inicio = Button(menu_lateral,
                      text="Inicio",
                      bg=f"#{cafe_claro}",
                      fg="black",
                      font=("Arial", 12),
                      relief="raised", command=mostrar_inicio)
boton_inicio.pack(pady=10,
                  padx=10,
                  fill="x")

boton_ingresos = Button(menu_lateral,
                        text="Ingresos",
                        bg=f"#{cafe_claro}",
                        fg="black",
                        font=("Arial", 12),
                        relief="raised",
                        command=mostrar_ingresos)
boton_ingresos.pack(pady=10,
                    padx=10,
                    fill="x")

boton_gastos = Button(menu_lateral,
                      text="Gastos",
                      bg=f"#{cafe_claro}",
                      fg="black",
                      font=("Arial", 12),
                      relief="raised",
                      command=mostrar_gastos)
boton_gastos.pack(pady=10,
                  padx=10,
                  fill="x")

boton_resultados = Button(menu_lateral,
                          text="Resultados",
                          bg=f"#{cafe_claro}",
                          fg="black",
                          font=("Arial", 12),
                          relief="raised",
                          command=mostrar_resultados)
boton_resultados.pack(pady=10,
                      padx=10,
                      fill="x")











# Comienza con la sección inicio
mostrar_inicio()

# Lanza la aplicación
aplicacion.mainloop()

