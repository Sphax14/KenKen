#Se realiza la importació de las librerias queson necesarias para el funcionamiento del programa
from tkinter import *
#from tkinter.ttk import *
from tkinter import  messagebox
import tkinter
import  webbrowser
#Se crea el menu principal del juego
class menu(tkinter.Tk):
    def __init__(menu):
        tkinter.Tk.__init__(menu)
        #Se establece el titulo de la vetana
        menu.title("Kenken: Menu Principal ")
        # Se define el tamaño que tendrá la ventana y se configura para que su tamaño no se pueda modificar
        menu.geometry("400x200")
        menu.resizable(width=False, height=False)
        # Se crea la barra del menu
        menubar = Menu(menu)
    # Se agregan la lista de comandos que tendra la barra del menu
        menubar.add_command(label="Jugar", command=menu.jugar)
        menubar.add_command(label="Configurar", command=menu.configurar)
        menubar.add_command(label="Ayuda", command=menu.ayuda)
        menubar.add_command(label="Acerca De", command=menu.acercaDe)
        menubar.add_command(label="Salir", command=menu.salir)
        # Se desplega el menú
        menu.config(menu=menubar)
        #Prueba valores por defecto config
        #Se abre el archivo que contiene las variables en el modo de lectura y se combierte al tipo lista
        configuracion=open("configuracion.dat","r")
        lista_config=list(configuracion.readline())
        configuracion.close() 
        # Se llama a las variable globales
        global dificultad
        global reloj
        global sonido
        #Se asigna a cada variable el ultimo valor almacenado en el archivo .dat
        dificultad =lista_config[0]
        reloj=lista_config[1]
        sonido=lista_config[2]
    # opción jugar, destruye la ventana actual y llama a la ventana Nombre
    def  jugar(menu):
        menu.destroy()
        nombre().mainloop()

    # opción configurar, destruye la ventana actual y crea la ventana configurar
    def configurar(menu):
        menu.destroy()
        configurar().mainloop()

    # opción ayuda; muestra al usuario una guía o manual de usuarío sobre el uso del programa
    def ayuda(menu):
        webbrowser.open_new(r"Manual_de_Usuario_Kenken.pdf")

    # opción acerca de; muestra el nombre del programa, la versión, la fecha de creación y el  nombre de los autores
    def acercaDe(menu):
        messagebox.showinfo("Acerca De", "Cronometro\nVersión: 1.7\nFecha: 02/10/2018 \nAutores: \nMarco Gamboa")

    # opción salir; destruye la ventana menu y finaliza la ejecución del programa
    def salir(menu):
       menu.quit()
#Se crea la ventana nombre
class nombre(tkinter.Tk):
    def  __init__(self):
        tkinter.Tk. __init__(self)
        #Se llama a la variable golbal nombreJugador y se establece como StringVar
        global  nombreJugador
        nombreJugador=StringVar()
        #Se detablece la ventana como no redimencionable, se establece el titulo y tamaño de la misma
        self.resizable(width=False, height=False)
        self.title("Jugador")
        self.geometry("300x80")
        #Se crea la caja de texto donde el usuario ingresara su nombre y se coloca en la ventana
        self.nombreJugador=Entry(self,width=20,textvariable=nombreJugador,font=("Arial Black",10),bg="chartreuse")
        self.nombreJugador.place(x=100,y=10)
        #Se crea la etiqueta nombre y se coloca en la ventana
        self.etiquetaNombre=Label(self,text="Nombre:",width=10,font=("Arial Black",10))
        self.etiquetaNombre.place(x=1,y=10)
        #Se crea el boton Aceptar y se coloca en la ventana
        self.bontonAceptar=Button(self,text="Aceptar",width=10,font=("Arial Black",10),command=self.aceptar,bg="cyan4",activebackground="magenta4")
        self.bontonAceptar.place(x=100,y=40)
    #Se define la función aceptardel boton Aceptar
    def aceptar(self):
        #Se obtiene el valor de la variable nombreJugador ingresada por el usuario
        nombreJugador=self.nombreJugador.get()
        #Se valida el valor de la variable nombreJugador
        if nombreJugador=="":
            #Si el usuario no dio un nombre y dio aceptar,
            #El programa usa el nombre de usuario "Player" como valor por defecto
            nombreJugador="Player"
        #Se destruye la ventana actual y se llama a la ventana jugar
        self.destroy()
        jugar().mainloop()
#Se crea la ventana Jugar
class jugar(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        #Se llama a las variables globales 
        global nombreJugador
        
        #Se establece la ventana como no redimencionable, se establece el titulo y tamaño de la misma
        self.resizable(width=False, height=False)
        self.title("Jugar")
        self.geometry("800x400")
        #Se crea la etiqueta con el nombre del programa
        self.etiquetaKenken=Label(self,text="KenKen",font=("Arial Black",30))
        self.etiquetaKenken.pack()
        #Se obtiene el valor ingresado por el usuario en la ventana nombre y se le asigna ese valor a la variable
        nombre=nombreJugador.get()
        #Si no se ingreso ningun valor en la ventana nombre se hace lo siguiente: 
        if nombre == "":
            #Se establece el nombre jugador como player y se coloca la etiqueta que muestra este dato en la ventana
            etiquetaNombre = Label(self, text=("Jugador: Player"), width=30, font=("Arial Black", 10))
            etiquetaNombre.place(x=10,y=310)
        #Si se ingreso información:
        else:
            #Se asigna el valor de la información a la etiqueta y se coloca en la ventana
            etiquetaNombre = Label(self, text=("Jugador:", nombre), width=30, font=("Arial Black", 10))
            etiquetaNombre.place(x=10,y=310)
        #Se muestra en pantalla la dificultad elegida
        #Se llama la variable global dificultad
        global dificulta5
        #Se evalua el valor de la variable dificultad y se imprime en pantalla
        try:
            nivel=int(dificultad)
            #Facil
            if nivel==0:
                etiqueta_Dificultad=Label(self,text="Dificultad: Facil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=90,y=350)
             #Intermedia
            elif nivel==1:
                etiqueta_Dificultad=Label(self,text="Dificultad: Intermedia",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=90,y=350)
            #Dificil
            elif nivel==2:
                etiqueta_Dificultad=Label(self,text="Dificultad: Dificil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=90,y=350)
        except:
            nivel=dificultad.get()
            #Facil
            if nivel==0:
                etiqueta_Dificultad=Label(self,text="Dificultad: Facil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=90,y=350)
             #Intermedia
            elif nivel==1:
                etiqueta_Dificultad=Label(self,text="Dificultad: Intermedia",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=90,y=350)
            #Dificil
            elif nivel==2:
                etiqueta_Dificultad=Label(self,text="Dificultad: Dificil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=90,y=350)
        #Se definen los botones que conforman la ventana
        # 1
        self.boton1=Button(self,text="1",width=5,font=("Arial Black",10),bg="gray")
        self.boton1.place(x=590,y=65)
        #2
        self.boton2=Button(self,text="2",width=5,font=("Arial Black",10),bg="gray")
        self.boton2.place(x=590,y=100)
        #3
        self.boton3=Button(self,text="3",width=5,font=("Arial Black",10),bg="gray")
        self.boton3.place(x=590,y=135)
        #4
        self.boton4=Button(self,text="4",width=5,font=("Arial Black",10),bg="gray")
        self.boton4.place(x=590,y=170)
        #5
        self.boton5=Button(self,text="5",width=5,font=("Arial Black",10),bg="gray")
        self.boton5.place(x=590,y=205)
        #6
        self.boton6=Button(self,text="6",width=5,font=("Arial Black",10),bg="gray")
        self.boton6.place(x=590,y=240)
       #Borrar
        self.botonBorrar=Button(self,text="Borrar",width=5,font=("Arial Black",10),bg="gray")
        self.botonBorrar.place(x=590,y=275)
        #Iniciar juego
        self.botonIniciar=Button(self,text="Iniciar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonIniciar.place(x=90,y=65)
        #Validar juego
        self.botonValidar=Button(self,text="Validar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonValidar.place(x=90,y=100)
        #Otro  juego
        self.botonOtro=Button(self,text="Otro Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonOtro.place(x=90,y=135)
        #Reiniciar juego
        self.botonReiniciar=Button(self,text="Reiciar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonReiniciar.place(x=90,y=170)
        #Terminar juego
        self.botonTerminar=Button(self,text="Terminar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonTerminar.place(x=90,y=205)
        #Top 10
        self.botonTop=Button(self,text="Top 10",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonTop.place(x=90,y=240)
        #Tamaño labels, intentar hacer recursivo
        horizontal = 55  # para cambia,font=("Arial Black", 10)r tamaño
        vertical = 40
        x = 240  # para cambiar ubicacion
        y = 65

        self.cuadro1 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro1.place(x=x, y=y)

        self.cuadro2 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro2.place(x=x + horizontal, y=y)

        self.cuadro3 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro3.place(x=x + horizontal * 2, y=y)

        self.cuadro4 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro4.place(x=x + horizontal * 3, y=y)

        self.cuadro5 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro5.place(x=x + horizontal * 4, y=y)

        self.cuadro6 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro6.place(x=x + horizontal * 5, y=y)

        self.cuadro7 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro7.place(x=x, y=y + vertical)

        self.cuadro8 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro8.place(x=x + horizontal, y=y + vertical)

        self.cuadro9 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro9.place(x=x + horizontal * 2, y=y + vertical)

        self.cuadro10 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro10.place(x=x + horizontal * 3, y=y + vertical)

        self.cuadro11 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro11.place(x=x + horizontal * 4, y=y + vertical)

        self.cuadro12 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro12.place(x=x + horizontal * 5, y=y + vertical)

        self.cuadro13 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro13.place(x=x, y=y + vertical * 2)

        self.cuadro14 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro14.place(x=x + horizontal, y=y + vertical * 2)

        self.cuadro15 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro15.place(x=x + horizontal * 2, y=y + vertical * 2)

        self.cuadro16 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro16.place(x=x + horizontal * 3, y=y + vertical * 2)

        self.cuadro17 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro17.place(x=x + horizontal * 4, y=y + vertical * 2)

        self.cuadro18 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro18.place(x=x + horizontal * 5, y=y + vertical * 2)

        self.cuadro19 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro19.place(x=x, y=y + vertical * 3)

        self.cuadro20 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro20.place(x=x + horizontal, y=y + vertical * 3)

        self.cuadro21 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro21.place(x=x + horizontal * 2, y=y + vertical * 3)

        self.cuadro22 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro22.place(x=x + horizontal * 3, y=y + vertical * 3)

        self.cuadro23 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro23.place(x=x + horizontal * 4, y=y + vertical * 3)

        self.cuadro24 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro24.place(x=x + horizontal * 5, y=y + vertical * 3)

        self.cuadro25 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro25.place(x=x, y=y + vertical * 4)

        self.cuadro26 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro26.place(x=x + horizontal, y=y + vertical * 4)

        self.cuadro27 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro27.place(x=x + horizontal * 2, y=y + vertical * 4)

        self.cuadro28 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro28.place(x=x + horizontal * 3, y=y + vertical * 4)

        self.cuadro29 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro29.place(x=x + horizontal * 4, y=y + vertical * 4)

        self.cuadro30 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro30.place(x=x + horizontal * 5, y=y + vertical * 4)

        self.cuadro31 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro31.place(x=x, y=y + vertical * 5)

        self.cuadro32 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro32.place(x=x + horizontal, y=y + vertical * 5)

        self.cuadro33 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro33.place(x=x + horizontal * 2, y=y + vertical * 5)

        self.cuadro34 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro34.place(x=x + horizontal * 3, y=y + vertical * 5)

        self.cuadro35 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro35.place(x=x + horizontal * 4, y=y + vertical * 5)

        self.cuadro36 = Entry(self, width=3, font=("Arial Black", 18))
        self.cuadro36.place(x=x + horizontal * 5, y=y + vertical * 5)
#   Se crea la clase configurar
class configurar(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        #Se establece el titulo de la ventana y el tamaño de la misma
        self.title("KenKen: Configuración")
        self.geometry("400x400")
        #Opción Dificultad
        #Se crea la etiqueta y se coloca en la ventana
        self.etiqueta_Dificultad=Label(self,text="Dificultad",font=("Arial Black",10))
        self.etiqueta_Dificultad.place(x=10,y=10)
        #Se llama la variable dificultad como global y se declara como IntVar
        global  dificultad
        dificultad=IntVar()
        #Se crean los RadioButtons
        #Dificultad Facil
        dFacil = Radiobutton(self,text='Facil', value=0, variable=dificultad)
        dFacil.place(x=10, y=30)
        #Dificultad Intermedia
        dIntermedia = Radiobutton(self,text='Intermedio', value=1, variable=dificultad)
        dIntermedia.place(x=10,y=50)
        #Dificultad Dificil
        dDificil = Radiobutton(self,text='Dificil', value=2, variable=dificultad)
        dDificil.place(x=10,y=70)
        #Opción Reloj
        #Se crea la etiqueta y se coloca en la ventana
        self.etiqueta_Reloj=Label(self,text="Reloj",font=("Arial Black",10))
        self.etiqueta_Reloj.place(x=10,y=90)
        #Se llama la variable reloj como global y se declara como IntVar
        global reloj
        reloj = IntVar()
        #Se crean los RadioButtons
        #Reloj Si
        rSi = Radiobutton(self,text='Si', value=0, variable=reloj) 
        rSi.place(x=10, y=120)
        #Reloj No
        rNo = Radiobutton(self,text='No', value=1, variable=reloj)
        rNo.place(x=10,y=140)
        #Reloj Timer
        rTimer = Radiobutton(self,text='Timer', value=2, variable=reloj)
        rTimer.place(x=10,y=160)
        #Opcion Sonido
        #Se crea y se coloca la etiqueta sonido
        self.etiqueta_Sonido=Label(self,text="Sonido",font=("Arial Black",10))
        self.etiqueta_Sonido.place(x=10,y=260)
        #Se llama la variable global sonido y se declara como IntVar
        global sonido
        sonido=IntVar()
        #Se crean los RadioButtons
        #Sonido No
        sNo= Radiobutton(self,text="No",value=0,variable=sonido)
        sNo.place(x=10,y=280)
        #Sonido Si
        sSi=Radiobutton(self,text="Si",value=1,variable=sonido)
        sSi.place(x=10,y=300)
        #Se crea el boton Jugar y se coloca en la ventana
        self.bontonJugar=Button(self,text="Jugar",command=self.jugar,font=("Arial Black",10),bg="gray")
        self.bontonJugar.place(x=120,y=330)
        #Se crea el boton menu y se coloca en la ventana
        self.botonMenu=Button(self,text="Menu",command=self.menu,font=("Arial Black",10),bg="gray",width=5)
        self.botonMenu.place(x=220,y=330)
    #Se define la función del Boton Jugar
    def jugar(self):
        #Al presionar el boton jugar esta función hace lo siguiente:
        #Abre el archivo que contiene guardadas las configuraciones en modo write
        configurar=open("configuracion.dat","w")
        #El archivo sobreescribe los valores anteriores con los valores actuales
        configurar.write(str(dificultad.get()))
        configurar.write(str(reloj.get()))
        configurar.write(str(sonido.get()))
        #Se cierra el archivo, quedando así  guardada la configuración establecida
        configurar.close()
        #Se destruye la ventana actual y crea la ventana nombre, para luego ir a la de jugar
        self.destroy()
        nombre().mainloop()
    #Se define la del boton menu
    def menu(self):
        #Al presionar el boton Menu esta función hace lo siguiente:
        #Abre el archivo que contiene guardadas las configuraciones en modo write
        configurar=open("configura","w")
        #El archivo sobreescribe los valores anteriores con los valores actuales
        configurar.write(str(dificultad.get()))
        configurar.write(str(reloj.get()))
        configurar.write(str(sonido.get()))
        #Se cierra el archivo, quedando así  guardada la configuración establecida
        configurar.close()
        #Se destruye la ventana actual y crea la ventana menu
        self.destroy()
        menu().mainloop() 
#Variable Globales del programa
nombreJugador="Player"
dificultad=0
reloj=0
sonido=0
menu().mainloop()