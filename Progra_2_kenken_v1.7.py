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
        global dimensiones
        #Se asigna a cada variable el ultimo valor almacenado en el archivo .dat
        dificultad =lista_config[0]
        reloj=lista_config[1]
        sonido=lista_config[2]
        dimensiones=lista_config[3]
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
        #Se lee el archivo.dat
        configuracion=open("configuracion.dat","r")
        lista_config=list(configuracion.readline())
        configuracion.close()
         #Se llama a la variable global dimensiones
        global dimensiones
        #Se asigna el valor a dimensiones
        dimensiones=lista_config[3]
        #Se llama a las variables global nombreJugador
        global nombreJugador
        #Se crea la cuadricula del juego 
        tt=Frame()
        tt.grid(column=0,row=0,padx=(200,200),pady=(50,50))
        tt.rowconfigure(0,weight=5)
        tt.columnconfigure(0,weight=5)
        dimensiones=str(dimensiones)
        if dimensiones=="0":
            n=6
        elif dimensiones=="1":
            n=3
        elif dimensiones=="2":
            n=4
        elif dimensiones=="3":
            n=5
        elif dimensiones=="4":
            n=7
        elif dimensiones=="5":
            n=8
        elif dimensiones=="6":
            n=9
        elif dimensiones=="7":
            n=10
        #Se crean las celdas con las dimiensiones indicadas
        if n<10:
            for i in range (1,n+1):
                for j in range(1,n+1):
                    nombre="c"+str(i)+str(j)
                    nombre=Entry(tt,text=nombre,width=3, font=("Arial Black", 18))
                    nombre.grid(column=j,row=i)

        #Se establece la ventana como no redimencionable, se establece el titulo y tamaño de la misma
        self.resizable(width=False, height=False)
        self.title("Jugar")
        self.geometry("800x400")



 # Leer partidas del archivo kenken_juegos.dat y almacenarla en un diccionario:
# llave del diccionario: nivel de la partida y un consecutivo
# valor del diccionario: otro diccionario con el detalle de la partida
# Estructura del diccionario del detalle de la partida:
# llave: numero de la jaula
# valor: operacion de la jaula y casillas que la componen 

        f = open("kenken_juegos2.dat")
        numero_partida = 0   # consecutivo para cada partida en el diccionario
        partidas = {}   # diccionario con todas las partidas
        while True:
            l = f.readline()
            if l=="": break  # EOF fin de archivo
            n = l[0] # nivel de la partida
            d = eval(l[2:-1]) # diccionario de esta partida
            numero_partida = numero_partida + 1
            partidas [n + str(numero_partida)]=d
        f.close()

        # ver el diccionario de partidas
        for d in partidas:
            print("Nivel de la partida:", d[0],"     consecutivo:", d[1:])
            p = partidas[d]
            for e in p:
                print(e,p[e])
        #Se crea la etiqueta con el nombre del programa
        self.etiquetaKenken=Label(self,text="KenKen",font=("Arial Black",30),fg="Dark Blue")
        self.etiquetaKenken.place(x=10,y=5)
        #Se obtiene el valor ingresado por el usuario en la ventana nombre y se le asigna ese valor a la variable
        nombre=nombreJugador.get()
        #Si no se ingreso ningun valor en la ventana nombre se hace lo siguiente: 
        if nombre == "":
            #Se establece el nombre jugador como player y se coloca la etiqueta que muestra este dato en la ventana
            etiquetaNombre = Label(self, text=("Jugador: Player"), font=("Arial Black", 10))
            etiquetaNombre.place(x=5,y=320)
        #Si se ingreso información:
        else:
            #Se asigna el valor de la información a la etiqueta y se coloca en la ventana
            etiquetaNombre = Label(self, text=("Jugador:", nombre), font=("Arial Black", 10))
            etiquetaNombre.place(x=5,y=320)
        #Se muestra en pantalla la dificultad elegida
        #Se llama la variable global dificultad
        global dificultad
        #Se evalua el valor de la variable dificultad y se imprime en pantalla
        try:
            nivel=int(dificultad)
            #Facil
            if nivel==0:
                etiqueta_Dificultad=Label(self,text="Dificultad: Facil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=5,y=350)
             #Intermedia
            elif nivel==1:
                etiqueta_Dificultad=Label(self,text="Dificultad: Intermedia",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=5,y=350)
            #Dificil
            elif nivel==2:
                etiqueta_Dificultad=Label(self,text="Dificultad: Dificil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=5,y=350)
        except:
            nivel=dificultad.get()
            #Facil
            if nivel==0:
                etiqueta_Dificultad=Label(self,text="Dificultad: Facil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=5,y=350)
             #Intermedia
            elif nivel==1:
                etiqueta_Dificultad=Label(self,text="Dificultad: Intermedia",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=5,y=350)
            #Dificil
            elif nivel==2:
                etiqueta_Dificultad=Label(self,text="Dificultad: Dificil",font=("Arial Black", 10))
                etiqueta_Dificultad.place(x=5,y=350)
        #Se definen los botones que conforman la ventana
        # 1
        self.boton1=Button(self,text="1",width=5,font=("Arial Black",10),bg="gray",command=self.uno)
        self.boton1.place(x=740,y=65)
        #2
        self.boton2=Button(self,text="2",width=5,font=("Arial Black",10),bg="gray",command=self.dos)
        self.boton2.place(x=740,y=100)
        #3
        self.boton3=Button(self,text="3",width=5,font=("Arial Black",10),bg="gray",command=self.tres)
        self.boton3.place(x=740,y=135)
        #4
        self.boton4=Button(self,text="4",width=5,font=("Arial Black",10),bg="gray",command=self.cuatro)
        self.boton4.place(x=740,y=170)
        #5
        self.boton5=Button(self,text="5",width=5,font=("Arial Black",10),bg="gray",command=self.cinco)
        self.boton5.place(x=740,y=205)
        #6
        self.boton6=Button(self,text="6",width=5,font=("Arial Black",10),bg="gray",command=self.seis)
        self.boton6.place(x=740,y=240)
       #Borrar
        self.botonBorrar=Button(self,text="Borrar",width=5,font=("Arial Black",10),bg="gray")
        self.botonBorrar.place(x=740,y=275)
        #Iniciar juego
        self.botonIniciar=Button(self,text="Iniciar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonIniciar.place(x=5,y=65)
        #Validar juego
        self.botonValidar=Button(self,text="Validar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonValidar.place(x=5,y=100)
        #Otro  juego
        self.botonOtro=Button(self,text="Otro Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonOtro.place(x=5,y=135)
        #Reiniciar juego
        self.botonReiniciar=Button(self,text="Reiciar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonReiniciar.place(x=5,y=170)
        #Terminar juego
        self.botonTerminar=Button(self,text="Terminar Juego",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonTerminar.place(x=5,y=205)
        #Top 10
        self.botonTop=Button(self,text="Top 10",width=14,font=("Arial Black",10),bg="Light gray")
        self.botonTop.place(x=5,y=240)

    #Se define la funcion asociada a cada boton
    #1
    def uno(self):
        print("1")
    #2
    def dos(self):
        print("2")
    #3
    def tres(self):
        print("3")
     #4
    def cuatro(self):
         print ("4")
    #5
    def cinco(self):
        print("5")
    #6
    def seis(self):
         print("6")
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
        #Pronostico de tiempo:
        global h
        global m
        global s
        #Se colocan los Spinbox y etiquetaas para tomar el pronostico del tiempo
        self.etiqueta_Timer=Label(self,text="Tiempo a utilizar:",font=("Arial Black",10))
        self.etiqueta_Timer.place(x=10,y=200)
        #Horas
        h=Spinbox(self, from_=0, to=23,width=4)
        h.place(x=20,y=270)
        self.etiqueta_Horas=Label(self,text="H",font=("Arial Black",10))
        self.etiqueta_Horas.place(x=30,y=240)
        #Minutos
        m =Spinbox(self, from_=0, to=59,width=4)
        m.place(x=70,y=270)
        self.etiqueta_Minutos=Label(self,text="M",font=("Arial Black",10))
        self.etiqueta_Minutos.place(x=80,y=240)
        #Segundos
        s = Spinbox(self, from_=0, to=59,width=4)
        s.place(x=120,y=270)
        self.etiqueta_Segundos=Label(self,text="S",font=("Arial Black",10))
        self.etiqueta_Segundos.place(x=130,y=240)
        #Opcion Sonido
        #Se crea y se coloca la etiqueta sonido
        self.etiqueta_Sonido=Label(self,text="Sonido",font=("Arial Black",10))
        self.etiqueta_Sonido.place(x=200,y=10)
        #Se llama la variable global sonido y se declara como IntVar
        global sonido
        sonido=IntVar()
        #Se crean los RadioButtons
        #Sonido No
        sNo= Radiobutton(self,text="No",value=0,variable=sonido)
        sNo.place(x=200,y=50)
        #Sonido Si
        sSi=Radiobutton(self,text="Si",value=1,variable=sonido)
        sSi.place(x=200,y=30)
        #Se crea el boton Jugar y se coloca en la ventana
        self.bontonJugar=Button(self,text="Jugar",command=self.jugar,font=("Arial Black",10),bg="gray")
        self.bontonJugar.place(x=120,y=330)
        #Se crea el boton menu y se coloca en la ventana
        self.botonMenu=Button(self,text="Menu",command=self.menu,font=("Arial Black",10),bg="gray",width=5)
        self.botonMenu.place(x=220,y=330)
        #Opción dimensiones 
        #Se crea y se coloca la etiqueta sonido
        self.etiqueta_Dimensiones=Label(self,text="Tamaño",font=("Arial Black",10))
        self.etiqueta_Dimensiones.place(x=200,y=90)
        #Se llama a la variable global dimensiones y se declara como IntVar
        global dimensiones
        dimensiones=IntVar()
        #Se crean los RadioButtons
        #3x3
        dm3= Radiobutton(self,text="3x3",value=1,variable=dimensiones)
        dm3.place(x=200,y=120)
        #4x4
        dm4= Radiobutton(self,text="4x4",value=2,variable=dimensiones)
        dm4.place(x=200,y=140)
        #5x5
        dm5= Radiobutton(self,text="5x5",value=3,variable=dimensiones)
        dm5.place(x=200,y=160)
        #6x6
        dm6= Radiobutton(self,text="6x6",value=0,variable=dimensiones)
        dm6.place(x=200,y=180)
        #7x7
        dm7= Radiobutton(self,text="7x7",value=4,variable=dimensiones)
        dm7.place(x=200,y=200)
        #8x8
        dm8= Radiobutton(self,text="8x8",value=5,variable=dimensiones)
        dm8.place(x=200,y=220)
        #9x9
        dm9= Radiobutton(self,text="9x9",value=6,variable=dimensiones)
        dm9.place(x=200,y=240)
        #Multitamaño
        dmMulti= Radiobutton(self,text="Multitamaño",value=7,variable=dimensiones)
        dmMulti.place(x=200,y=260)
    #Se define la función del Boton Jugar
    def jugar(self):
        #Al presionar el boton jugar esta función hace lo siguiente:
        #Abre el archivo que contiene guardadas las configuraciones en modo write
        configurar=open("configuracion.dat","w")
        #El archivo sobreescribe los valores anteriores con los valores actuales
        configurar.write(str(dificultad.get()))
        configurar.write(str(reloj.get()))
        configurar.write(str(sonido.get()))
        configurar.write(str(dimensiones.get()))
        #Se cierra el archivo, quedando así  guardada la configuración establecida
        configurar.close()
        #Se destruye la ventana actual y crea la ventana nombre, para luego ir a la de jugar
        self.destroy()
        nombre().mainloop()
    #Se define la del boton menu
    def menu(self):
        #Al presionar el boton Menu esta función hace lo siguiente:
        #Abre el archivo que contiene guardadas las configuraciones en modo write
        configurar=open("configuracion.dat","w")
        #El archivo sobreescribe los valores anteriores con los valores actuales
        configurar.write(str(dificultad.get()))
        configurar.write(str(reloj.get()))
        configurar.write(str(sonido.get()))
        configurar.write(str(dimensiones.get()))
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
dimensiones=0
h=0
m=0
s=0
menu().mainloop()
