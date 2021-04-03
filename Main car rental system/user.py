from tkinter import *
class User(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.f=Frame(root,height=1000,width=1200,bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()

        l1=Label(self.f,text='LOGGED IN USER' ,font=('Bold'),bg='sandybrown',)
        l1.place(x=500,y=150)

        b1=Button(self.f,text='BOOK CAR',width=20,height=2,activebackground='gray',activeforeground='red',command=self.book,bg='brown')
        b2=Button(self.f,text='RETURN CAR',width=20,height=2,activebackground='gray',activeforeground='red',bg='brown',command=self.remove)
        b3 = Button(self.f, text='LOGOUT ', width=20, height=2, activebackground='gray',activeforeground='red',command=self.logout,bg='red')

        b1.place(x=400,y=300)
        b2.place(x=600, y=300)
        b3.place(x=500,y=400)


    def logout(self):
        import loginuser
        self.f.destroy()
        loginuser.Login(self.master)

    def book(self):
        import book
        self.f.destroy()
        book.book(self.master)

    def remove(self):
        import Return
        self.f.destroy()
        Return.Return(self.master)



