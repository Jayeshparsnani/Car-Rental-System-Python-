from tkinter import *
import tkinter.messagebox
from defaultpage import *


class Add(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.abc()
    def abc(self):
        self.l0 = Label(self.panel, text="ADD CAR", bg='red', font=("bold", 20))
        self.l1 = Label(self.panel, text="Car Name:", bg='red')
        self.l2 = Label(self.panel, text="Mileage:", bg='red')
        self.l3 = Label(self.panel, text="Model No.:", bg='red')
        self.l4 = Label(self.panel, text="Availability:", bg='red')

        self.e1 = Entry(self.panel,bg='sandybrown', width=25,fg="black")
        self.e2 = Entry(self.panel, width=25, bg="sandybrown", fg="black")
        self.e3 = Entry(self.panel, width=40, bg="sandybrown", fg="black")
        self.e4 = Entry(self.panel, width=25, bg="sandybrown", fg="black")

        self.l0.place(x=520, y=20)
        self.l1.place(x=420, y=90)
        self.l2.place(x=420, y=140)
        self.l3.place(x=420, y=190)
        self.l4.place(x=420, y=240)

        self.e1.place(x=600, y=90, height=25, width=200)
        self.e2.place(x=600, y=140, height=25, width=200)
        self.e3.place(x=600, y=190, height=25, width=200)
        self.e4.place(x=600, y=240, height=25, width=200)

        self.b = Button(self.panel, text="Add Car", width="20", height="2",
                        activebackground='gray', activeforeground='red', bg='brown')

        self.b.place(x=400, y=330)
        b1 = Button(self.f, text='Back', height=2, width=20, activebackground='gray',
                    activeforeground='red', bg='red')
        b1.place(x=700, y=330)

root=Tk()
m=Add(root)
root.mainloop()
