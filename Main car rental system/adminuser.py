from tkinter import *


class switch(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.f=Frame(root,height=1000,width=1200,bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()

        self.b1 = Button(self.f, text="User Login", width=20, height=2, activebackground='gray',activeforeground='red', command=self.user,bg='brown')
        self.b2 = Button(self.f, text="Admin Login", width=20, height=2,activebackground='gray',activeforeground='red', command=self.admin,bg='brown')
        self.b3 = Button(self.f, text='HOME ', width=20, height=2, activebackground='gray', activeforeground='red',
                    command=self.home, bg='red')

        self.b1.place(x=400, y=300)
        self.b2.place(x=650, y=300)
        self.b3.place(x=520, y=400)

    def user(self):
        import loginuser
        self.f.destroy()
        loginuser.Login(self.master)

    def admin(self):
        import loginadmin
        self.f.destroy()
        loginadmin.Login1(self.master)

    def home(self):
        import home
        self.f.destroy()
        home.Home(self.master)



