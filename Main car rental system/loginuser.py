from tkinter import *
import tkinter.messagebox

import sqlite3

conn = sqlite3.connect('test.db')
print("CONNECTED!!!")


class Login(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.f = Frame(root, height=1000, width=1200, bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()

        self.l0 = Label(self.f, text="USER LOGIN PAGE", bg='sandybrown',font=("bold", 20))
        self.l1 = Label(self.f, text="Username:", bg='sandybrown')
        self.l2 = Label(self.f, text="Password:", bg='sandybrown')

        self.e4 = Entry(self.f, width=25, bg="white", fg="black", font=("Arial", 14))
        self.e5 = Entry(self.f, width=25, bg="white", fg="black", show='*')

        self.l0.place(x=480, y=190)
        self.l1.place(x=450, y=270)
        self.l2.place(x=450, y=310)

        self.e4.place(x=570, y=270,height=25,width=200)
        self.e5.place(x=570, y=310,height=25,width=200)

        self.b = Button(self.f, text="Login", width="20", height="2", command=self.checklogin, activebackground='gray',
                        activeforeground='red', bg='brown')

        self.b.place(x=430, y=400)
        b1 = Button(self.f, text='BACK', height=2, width=20, command=self.home, activebackground='gray',
                    activeforeground='red', bg='red')
        b1.place(x=670, y=400)

    def login(self):
        import user
        self.f.destroy()
        user.User(self.master)

    def checklogin(self):

        if self.e4.get() == "" or self.e5.get() == "":
            tkinter.messagebox.showinfo("Error", "PLEASE FILL ALL THE CREDENTIALS")
        else:

            query = str("SELECT * FROM register WHERE register_username=? AND register_password=?")
            r = conn.execute(query, (self.e4.get(), self.e5.get()))
            conn.commit()
            data = r.fetchall()
            if not data:
                tkinter.messagebox.showerror("Wrong Credentials!", "INVALID EMAIL OR PASSWORD")
            #for i in data:
                #if self.e4.get() == i[5] or self.e5.get() == i[3]:
                   # self.login()
                  #  break

            else:
                for i in data:
                    if self.e4.get() == i[5] or self.e5.get() == i[3]:
                        self.login()

                    #tkinter.messagebox.showerror("Wrong Credentials!", "INVALID EMAIL OR PASSWORD")
                   # break

    def home(self):
        import adminuser
        self.f.destroy()
        adminuser.switch(self.master)

