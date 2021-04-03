from defaultpage import *
from tkinter import *

class Adminlogin(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.widgets()

    def widgets(self):

        self.l0 = Label(self.panel, text="ADMIN LOGIN PAGE", bg='red',font=("bold", 20))
        self.l1 = Label(self.panel, text="Username:", bg='red')
        self.l2 = Label(self.panel, text="Password:", bg='red')

        self.e1 = Entry(self.panel,bg="white", fg="black",width=25, font=("Arial", 14))
        self.e2 = Entry(self.panel, bg="white", fg="black",width=25, show='*')

        self.l0.place(x=480, y=190)
        self.l1.place(x=450, y=270)
        self.l2.place(x=450, y=310)

        self.e1.place(x=570, y=270,height=25,width=200)
        self.e2.place(x=570, y=310,height=25,width=200)

        self.b = Button(self.panel, text="Login", width="20", height="2",  activebackground='gray',
                        activeforeground='red', bg='brown')

        self.b.place(x=450, y=380)
        b1 = Button(self.panel, text='HOME', height=2, width=20, bg='red')
        b1.place(x=670, y=380)
