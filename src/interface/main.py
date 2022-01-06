import tkinter
from tkinter import *
from PIL import Image, ImageTk
from math import *

application = Tk()
application.title("NUMERICAL METHODS") #MAIN WINDOW TITLE, TITULO DE LA VENTANA PRINCIPAL
application.geometry("700x500") # WINDOW'S DIMENTIONS, DIMENSIONES DE LA VENTANA

#SWIPE FRAME, MARCO DESLIZABLE
widthframe_min = 50  # minimum width of the frame, MINIMO ANCHO DEL MARCO DESLIZABLE
widthframe_max = 150 # maximum width of the frame, MAXIMO ANCHO DEL MARCO DESLIZABLE
incre_width = widthframe_min # increasing width of the frame, INCREMENTO DEL ANCHO DEL MARCO
extensive = False # check if the frame is completetly expanded, REVISAR SI EL MARCO ESTA COMPLETAMENTE EXTENDIDO


def extensiv():          # FUNCION PARA EXTENDER MARCO
    global incre_width, extensive # INDICAMOS LAS VAR GLOBALES PARA QUE PUEDAN SER MODIFICADAS DENTRO DE LA FUNCIÓN 
    incre_width += 10  # increase the width by 15, INCREMENTO DEL ANCHO POR 15 UNIDADES
    rep = application.after(5, extensiv) # Repeat this function every 5ms, LLAMAR CADA 5 ms LA FUNCIÓN 
    frame_one.config(width=incre_width) # change the width to new increase width, CAMBIAR EL ANCHO A UN NUEVO INCREMENTO DE ANCHO
    if incre_width >= widthframe_max: #if width is greater than maximum width, SI EL ANCHO ES MAYOR QUE EL ANCHO MAXIMO 
        extensive = True # frame is expanded, EL MARCO DESLIZABLE ESTA EXTENDIDO
        application.after_cancel(rep) #stop repeating the function, DETENER LA ACTUALIZACION DE CADA 5 ms DE LA FUNCION 
        cover()


def contract():
    global incre_width, extensive
    incre_width -= 10 # reduce the width by 15, DISMINUCION DEL ANCHO POR 15 UNIDADES
    rep = application.after(5, contract) # call this function every 5 ms, LLAMAR ESTA FUNCION CADA 5ms
    frame_one.config(width=incre_width) # change the width to new reduced width, CAMBIAR EL ANCHO A UN NUEVA REDUCCION DE ANCHO
    if incre_width <= widthframe_min: #if width is smaller than minimum width, SI EL ANCHO ES Menor QUE EL ANCHO Minimo 
        extensive = False # The frame is not extended, EL MARCO NO ESTA EXTENDIDO 
        application.after_cancel(rep) # STOP REPEATING THE FUNCTION, detener la actualizacion/llamado de cada 5 ms de la funcion
        cover()


def cover():
    if extensiv:
        home_b.config(text='Function',image='',font=(0,10))
        set_b.config(text='Guide',image='',font=(0,10))
        ring_b.config(text='Help',image='',font=(0,10))
    elif contract:
        home_b.config(image=home,font=(0,15))
        set_b.config(image=settings,font=(0,15))
        ring_b.config(image=ring,font=(0,15))

home = ImageTk.PhotoImage(Image.open('/home/samir/Documentos/Numerical_methods_py/src/interface/function.png').resize((40,40),Image.ANTIALIAS))
settings = ImageTk.PhotoImage(Image.open('/home/samir/Documentos/Numerical_methods_py/src/interface/settings.png').resize((40,40),Image.ANTIALIAS))
ring = ImageTk.PhotoImage(Image.open('/home/samir/Documentos/Numerical_methods_py/src/interface/guide.png').resize((40,40),Image.ANTIALIAS))


application.update() # For the width to get update 
frame_one = Frame(application, bg='DimGray', width=50, height=application.winfo_height(), borderwidth=3, highlightthickness=0)
frame_one.pack(side="left", fill="both", expand=False) 

# Make the buttons with the icons to be shown
home_b = Button(frame_one,image=home,bg='SlateGray',relief='raised',pady=4) 
set_b = Button(frame_one,image=settings,bg='SlateGray',relief='raised',pady=4)
ring_b = Button(frame_one,image=ring,bg='SlateGray',relief='raised',pady=4)

# Put them on the frame
home_b.pack(side="top")
set_b.pack(side="top")
ring_b.pack(side="top")
# Bind to the frame, if entered or left
frame_one.bind('<Enter>', lambda e: extensiv())
frame_one.bind('<Leave>', lambda e: contract())
# So that it does not depend on the widgets inside the frame
frame_one.pack_propagate(0)

# TITULO DENTRO DE LA INTERFAZ
myLabel1 = Label(application, text=" Welcome to numerical methods solutions aplication").pack(side="top", fill="x", expand=False) 
myLabel2 = Label(application, text="F(x)").pack(side="left", fill="y", expand=False, padx=10, pady=0)

# ENTRADA EN EL CAJA DE TEXTO
# str_box = StringVar()   
# str_box.set('Enter the funtion what you want to calculate') #default value in textbox can be actualized
entry = Entry(application ,width=50, bg="aliceblue", borderwidth=3)
entry.pack(side="left", padx=20, pady=10)


# #ACCIONES DE LOS BOTONES

def clickequal_button(function_name):
    current = entry.get()
    equation = current + function_name
    entry.delete(0, END)
    entry.insert(0, equation)
    #entry.insert(0, str(grados))

#ACCION DE LAS OPERACIONES: DIV,POTENCIA,RAIZ,TRIGONOMET...
def click_button(function_string):
    #entry.delete(0, END)
    #entry.insert(0, number)
    function = eval(function_string)
    myCLick = Label(application, text=function).pack(side=LEFT)
    print(function)
    #print(function_string)

def clicktwo_button():

    button_1 = Button(application, text="□/□", command=click_button, padx=10, pady=5).pack(side="bottom")
    button_2 = Button(application, text="□²", command=click_button, padx=10, pady=5).pack(side="bottom")
    button_3 = Button(application, text="□▫", command=click_button, padx=10, pady=5).pack(side="bottom")
    button_4 = Button(application, text="▫√", command=click_button, padx=10, pady=5).pack(side="bottom")
# PUT BUTTON ON THE SCREEN

def clickthree_button():

    '''' ARREGRAR EL ENLACE ENTRE EL BOTON TRIG Y LA CAJA DE TEXTO '''

    dropdown_two = Menubutton(application, text='')
    dropdown_two.menu = Menu(dropdown_two)
    dropdown_two['menu'] = dropdown_two.menu
    dropdown_two.menu.add_command(label='sen', command=lambda: clickequal_button('sin()'))
    dropdown_two.menu.add_command(label='cos', command=lambda: clickequal_button('cos()'))
    dropdown_two.config(relief='ridge',fg="white", bg="#111111", padx=3, pady=3, borderwidth=2, highlightthickness=10)
    dropdown_two.pack(side='left', padx=5, pady=5)
    
    # button_5 = Button(application, text="sin □", command=click_button, padx=10, pady=5).pack(side="bottom")
    # button_6 = Button(application, text="cos □", command=click_button, padx=10, pady=5).pack(side="bottom")
    # button_7 = Button(application, text="tan □", command=click_button, padx=10, pady=5).pack(side="bottom")
    # button_8 = Button(application, text="π", command= lambda: str_box, padx=10, pady=5).pack(side="bottom")

# #BUTTON'S DEFINITION
equal_button = Button(application, text="=", command= lambda: click_button(entry.get()), fg="white", bg="#111111", padx=3, pady=2, borderwidth=2, highlightthickness=6).pack(side="left")
#bmath_button = Button(application, text='√...', command=clicktwo_button, fg="white", bg="#111111", padx=3, pady=2, borderwidth=2, highlightthickness=6).pack(side="left")
#cmath_button = Button(application, text='TRIGONOMETRY', command=clickthree_button, fg="white", bg="#111111", padx=3, pady=2, borderwidth=2, highlightthickness=6).pack(side="left")

#DROP DOWN MATH MENU 

drop_down = Menubutton(application, text='Math Input')
drop_down.menu = Menu(drop_down)
drop_down['menu'] = drop_down.menu
drop_down.menu.add_command(label='TRIG', command=lambda: clickthree_button())
drop_down.menu.add_command(label='√', command=lambda: clicktwo_button())
drop_down.config(relief='ridge',fg="white", bg="#111111", padx=3, pady=3, borderwidth=2, highlightthickness=10)
drop_down.pack(side='left', padx=5, pady=5)


application.mainloop()


