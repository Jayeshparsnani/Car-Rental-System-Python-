from tkinter import *

import tkinter.messagebox


class Login1(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.f = Frame(root, height=1000, width=1200, bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()

        self.l0 = Label(self.f, text="ADMIN LOGIN PAGE", bg='sandybrown',font=("bold", 20))
        self.l1 = Label(self.f, text="Username:", bg='sandybrown')
        self.l2 = Label(self.f, text="Password:", bg='sandybrown')

        self.e1 = Entry(self.f,bg="white", fg="black",width=25, font=("Arial", 14))
        self.e2 = Entry(self.f, bg="white", fg="black",width=25, show='*')

        self.l0.place(x=480, y=190)
        self.l1.place(x=450, y=270)
        self.l2.place(x=450, y=310)

        self.e1.place(x=570, y=270,height=25,width=200)
        self.e2.place(x=570, y=310,height=25,width=200)

        self.b = Button(self.f, text="Login", width="20", height="2", command=self.checklogin, activebackground='gray',
                        activeforeground='red', bg='brown')

        self.b.place(x=450, y=380)
        b1 = Button(self.f, text='BACK', height=2, width=20, command=self.home, bg='red')
        b1.place(x=670, y=380)

    def home(self):
        import adminuser
        self.f.destroy()
        adminuser.switch(self.master)

    def user(self):
        import adminlog
        self.f.destroy()
        adminlog.Admin(self.master)

    def checklogin(self):
        username = self.e1.get()
        password = self.e2.get()

        if username == "" or password == "":
            tkinter.messagebox.showerror("Error", "PLEASE FILL ALL THE CREDENTIALS")

        else:

            if username == 'Admin' or password == 'dmcar':
                self.user()

            else:
                tkinter.messagebox.showerror("Wrong Credentials!", "INVALID EMAIL OR PASSWORD")

