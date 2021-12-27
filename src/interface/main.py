from tkinter import *
application = Tk()
application.title("NUMERICAL METHODS")
application.geometry("500x600")
# TITULO DENTRO DE LA INTERFAZ
myLabel1 = Label(application, text=" Welcome to numerical methods solutions aplication").pack(pady=20)
# ENTRADA EN EL CAJA DE TEXTO
entry = Entry(application, width=50, bg="aliceblue", borderwidth=3)
entry.insert(0, 'Enter the funtion what you want to calculate')
entry.pack()

#ACCIONES DE LOS BOTONES

def click_button():
    entry.delete(0, END)
    entry.insert(0, number)
    myCLick = Label(application, text='Has dado click!').pack()

def clicktwo_button():
    #myClick_two = Label(application, text='Has dado click!').pack()
    button_1 = Button(application, text="□/□", command=click_button(1), padx=10, pady=5).pack()
    button_2 = Button(application, text="□²", command=click_button(2), padx=10, pady=5).pack()
    button_3 = Button(application, text="□▫", command=click_button(3), padx=10, pady=5).pack()
    button_4 = Button(application, text="▫√", command=click_button(4), padx=10, pady=5).pack()
def clickthree_button():
    button_5 = Button(application, text="sin □", command=click_button(5), padx=10, pady=5).pack()
    button_6 = Button(application, text="cos □", command=click_button(6), padx=10, pady=5).pack()
    button_7 = Button(application, text="tan □", command=click_button(7), padx=10, pady=5).pack()
    button_8 = Button(application, text="π", command=click_button(8), padx=10, pady=5).pack()

#DEFINICION DE BOTONES
equal_Button = Button(application, text="=", command=click_button, fg="white", bg="#111111", padx=3, pady=2, borderwidth=2, highlightthickness=6).pack()
bmath_Button = Button(application, text='√...', command=clicktwo_button, fg="white", bg="#111111", padx=3, pady=2, borderwidth=2, highlightthickness=6).pack()
cmath_Button = Button(application, text='TRIGONOMETRY', command=clickthree_button, fg="white", bg="#111111", padx=3, pady=2, borderwidth=2, highlightthickness=6).pack()

application.mainloop()


