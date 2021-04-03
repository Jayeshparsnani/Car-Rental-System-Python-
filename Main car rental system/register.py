from tkinter import *
import tkinter.messagebox

import sqlite3
conn=sqlite3.connect('test.db')
print("CONNECTED!!!")

class Register(Frame):

    def __init__(self,root):
        Frame.__init__(self,root)
        self.f=Frame(root,height=1000,width=1200,bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()


        self.l0=Label(self.f,text="REGISTER",bg='sandybrown',font=('bold',20))
        self.l1=Label(self.f,text="Name:",bg='sandybrown')
        self.l2 = Label(self.f,text="Phn.no:",bg='sandybrown')
        self.l3 = Label(self.f,text="Address:",bg='sandybrown')
        self.l4 = Label(self.f,text="Username:",bg='sandybrown')
        self.l5 = Label(self.f,text="password:",bg='sandybrown')
        self.l6 = Label(self.f,text="Confirm Password:",bg='sandybrown')

        self.e1=Entry(self.f,width=25,bg="white",font=("Arial",14))
        self.e2 = Entry(self.f, width=25, bg="white", fg="black")
        self.e3 = Entry(self.f, width=40, bg="white", fg="black")
        self.e4 = Entry(self.f, width=25, bg="white", fg="black", font=("Arial", 14))
        self.e5 = Entry(self.f, width=25, bg="white", fg="black",show='*')
        self.e6 = Entry(self.f, width=25, bg="white", fg="black",show='*')

        self.l0.place(x=520,y=80)
        self.l1.place(x=420,y=150)
        self.l2.place(x=420, y=200)
        self.l3.place(x=420, y=250)
        self.l4.place(x=420,y=300)
        self.l5.place(x=420, y=350)
        self.l6.place(x=420, y=400)
        self.e1.place(x=600, y=150,height=25,width=200)
        self.e2.place(x=600, y=200,height=25,width=200)
        self.e3.place(x=600, y=250,height=25,width=200)
        self.e4.place(x=600, y=300,height=25,width=200)
        self.e5.place(x=600, y=350,height=25,width=200)
        self.e6.place(x=600, y=400,height=25,width=200)


        self.b=Button(self.f,text="Register",width="20",height="2",command=self.insertdetails,activebackground='gray',activeforeground='red',bg='brown')

        self.b.place(x=400,y=500)
        b1 = Button(self.f, text='HOME', height=2, width=20, command=self.home,activebackground='gray',activeforeground='red',bg='red')
        b1.place(x=700, y=500)

    def home(self):
        import home
        self.f.destroy()
        home.Home(self.master)

    def login(self):
        import loginuser
        self.f.destroy()
        loginuser.Login(self.master)

    def insertdetails(self):  # registration
        name = self.e1.get()
        addr = self.e3.get()
        mobile = self.e2.get()
        username = self.e4.get()
        password = self.e5.get()
        rpassword = self.e6.get()
        if name == '' or addr == '' or mobile == '' or password == '' or rpassword == ''or username=='':
            tkinter.messagebox.showinfo("Error", "Please Enter all the details")
        else:

            try:
                query = str(
                    "INSERT INTO register(register_name, register_mobile, register_addr, register_password,register_username, register_rpassword ) VALUES(?,?,?,?,?,?)")
                conn.execute(query, (name,mobile,addr, password,username, rpassword))
                conn.commit()
            except sqlite3.IntegrityError:
                tkinter.messagebox.showinfo("Error", "The entered Registration is already present")
            else:
                if rpassword == password:
                    print("registered")
                    tkinter.messagebox.showinfo("SUCCESSFUL", "REGISTRATION DONE SUCCESSFULLY")
                    self.login()
                else:
                    tkinter.messagebox.showinfo("Error", "The re-entered password doesnt match previous password")


def create_table():
    register_query = str("CREATE TABLE IF NOT EXISTS register(register_name VARCHAR(20)," +
                        "register_mobile INTEGER," +
                        "register_addr VARCHAR(20)," +
                        "register_password VARCHAR(20)," +
                        "register_username VARCHAR(20) PRIMARY KEY," +
                        "register_rpassword VARCHAR(20))")

    conn.execute(register_query)
    print("created client table")

create_table()