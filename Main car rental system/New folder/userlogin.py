from defaultpage import *
from tkinter import *

class Userlogin(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.userwidgets()

    def userwidgets(self):
        self.l0 = Label(self.panel, text="USER LOGIN PAGE", bg='red',font=("bold", 20))
        self.l1 = Label(self.panel, text="Username:", bg='red')
        self.l2 = Label(self.panel, text="Password:", bg='red')

        self.e4 = Entry(self.panel, width=25, bg="white", fg="black", font=("Arial", 14))
        self.e5 = Entry(self.panel, width=25, bg="white", fg="black", show='*')

        self.l0.place(x=480, y=190)
        self.l1.place(x=450, y=270)
        self.l2.place(x=450, y=310)

        self.e4.place(x=570, y=270,height=25,width=200)
        self.e5.place(x=570, y=310,height=25,width=200)

        self.b = Button(self.panel, text="Login", width="20", height="2", activebackground='gray',
                        activeforeground='red', bg='brown')

        self.b.place(x=430, y=400)
        b1 = Button(self.panel, text='HOME', height=2, width=20, activebackground='gray',
                    activeforeground='red', bg='red')
        b1.place(x=670, y=400)


root=Tk()
c=Userlogin(root)
root.mainloop()
