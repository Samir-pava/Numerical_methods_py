import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from math import *

application = tk.Tk()
application.title("NUMERICAL METHODS") #MAIN WINDOW TITLE, TITULO DE LA VENTANA PRINCIPAL
application.geometry("700x500") # WINDOW'S DIMENTIONS, DIMENSIONES DE LA VENTANA
application.config(bg='White')
scroll_barVer = tk.Scrollbar(application, orient = tk.VERTICAL)
scroll_barVer.pack(side= tk.RIGHT, fill = 'y')
scroll_barHor = tk.Scrollbar(application, orient = tk.HORIZONTAL)
scroll_barHor.pack(side= tk.BOTTOM, fill = 'x')

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
frame_one = Frame(application, bg='Goldenrod', width=50, height=application.winfo_height(), borderwidth=3, highlightthickness=0)
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
title_image = ImageTk.PhotoImage(Image.open('/home/samir/Documentos/Numerical_methods_py/src/interface/title.png').resize((450,100),Image.ANTIALIAS))
title_label = Label(application,image=title_image, bg='White')
title_label.pack(side='top', pady=20)

#myLabel1 = Label(application, text=" Welcome to numerical methods solutions aplication").pack(side="top", expand=False) 
myLabel2 = Label(application, text="F(x)").pack(side="top", expand=False, ipadx=0, ipady=0)

# ENTRADA EN EL CAJA DE TEXTO
# str_box = StringVar()   
# str_box.set('Enter the funtion what you want to calculate') #default value in textbox can be actualized
entry = Entry(application ,width=40, fg="Crimson", borderwidth=1, font=("helvetica", 12,'bold'), highlightthickness=2, highlightcolor='Crimson')
entry.pack(side="top", padx=0, pady=10)


# #ACCIONES DE LOS BOTONES
#ACCION DE INGRESAR VALORES DEL DROP DOWN MENU HACIA LA CAJA DE TEXTO 
def click_button(function_name):
    current = entry.get()
    equation = current + function_name
    entry.delete(0, END)
    entry.insert(0, equation)
    #entry.insert(0, str(grados))

#ACCION DEL BOTON IGUAL =
def clickequal_button(function_string):
    #entry.delete(0, END)
    #entry.insert(0, number)
    function = eval(function_string)
    myCLick = Label(application, text=function).pack(side=LEFT)
    print(function)
    #print(function_string)

def clicktwo_button():
    pass

# PUT BUTTON ON THE SCREEN

def clickthree_button():
    pass
   

# #BUTTON'S DEFINITION
equal_button = Button(application, text="=", font=("Times", 16,'bold'), relief='flat', command= lambda: clickequal_button(entry.get()), fg="Crimson", bg="White", padx=6, pady=2, borderwidth=0, highlightthickness=0).pack(side="top")

#DROP DOWN MATH MENU 

drop_down = Menubutton(application, text='...', underline=4, font=("Times", 17,'bold'))
drop_down.config(relief='flat',fg="Crimson", bg="White", padx=2, pady=2, borderwidth=2, highlightthickness=0)
drop_down.pack(side='top', padx=2, pady=2)
drop_down.menu = Menu(drop_down)
drop_down.menu.config(bg="Goldenrod", fg="MidnightBlue", tearoff=0)
#drop_down.menu.border=False
drop_down.menu.choices = Menu(drop_down.menu)
drop_down.menu.choices.config(bg="Goldenrod", fg="MidnightBlue", tearoff=0)
drop_down.menu.choices.wierdones = Menu(drop_down.menu)
drop_down.menu.choices.wierdones.config(bg="Goldenrod", fg="MidnightBlue", tearoff=0)
#drop_down.menu.choices.wierdones = Menu(drop_down.menu.choices)

drop_down.menu.choices.wierdones.add_command(label='sen', command=lambda: click_button('sin( )'))
drop_down.menu.choices.wierdones.add_command(label='cos', command=lambda: click_button('cos( )'))
drop_down.menu.choices.wierdones.add_command(label='tan', command=lambda: click_button('tan( )'))
drop_down.menu.choices.wierdones.add_command(label='sen^-1', command=lambda: click_button('asin( )'))
drop_down.menu.choices.wierdones.add_command(label='cos^-1', command=lambda: click_button('acos( )'))
drop_down.menu.choices.wierdones.add_command(label='tan^-1', command=lambda: click_button('atan( )'))
drop_down.menu.choices.wierdones.add_command(label='π', command=lambda: click_button('pi'))

drop_down.menu.choices.add_command(label='√ ', command=lambda: click_button('sqrt( )'))
drop_down.menu.choices.add_command(label='log10', command=lambda: click_button('log10( )'))
drop_down.menu.choices.add_command(label='ln', command=lambda: click_button('log1p( )'))
drop_down.menu.choices.add_command(label='π', command=lambda: click_button('pi'))
drop_down.menu.choices.add_command(label='ⅇ', command=lambda: click_button('e'))
drop_down.menu.choices.add_command(label='τ', command=lambda: click_button('tau'))

drop_down.menu.add_cascade(label='Trigonometric functions', menu=drop_down.menu.choices.wierdones)
drop_down.menu.add_cascade(label='Operator', menu=drop_down.menu.choices)



drop_down['menu'] = drop_down.menu





application.mainloop()


