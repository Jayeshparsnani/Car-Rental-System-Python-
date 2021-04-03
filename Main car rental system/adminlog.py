from tkinter import *
import sqlite3

conn = sqlite3.connect('test.db')
print("CONNECTED!!!")


class Admin(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.f = Frame(root, height=1000, width=1200,bg='sandybrown')
       
        self.f.pack()

        self.l1 = Label(self.f, text="Admin Logged In",font=('bold',16),bg='sandybrown')
        self.b1 = Button(self.f, text="Add car",width=20,height=2,activebackground='gray',activeforeground='red',bg='brown',command=self.add)
        self.b2 = Button(self.f, text="Delete car",width=20,height=2,activebackground='gray',activeforeground='red',bg='brown',command=self.delete)
        self.b3 = Button(self.f, text="Logout", width=20, height=2,activebackground='gray',activeforeground='red',command=self.logout,bg='red')
        self.b4 = Button(self.f, text="Users", width=20, height=2, activebackground='gray',activeforeground='red',bg='brown',command=self.usr)

        self.l1.place(x=500,y=150)
        self.b1.place(x=300, y=250)
        self.b2.place(x=700, y=250)
        self.b3.place(x=500, y=350)
        self.b4.place(x=500, y=250)

    def logout(self):
        import loginadmin
        self.f.destroy()
        loginadmin.Login1(self.master)

    def delete(self):
        import delete
        self.f.destroy()
        delete.Delete(self.master)

    def add(self):
        import add
        self.f.destroy()
        add.Add(self.master)

    def usr(self):
        import display

        self.f.destroy()
        display.display(self.master)


#root = Tk()
#mb = Admin(root)

#root.mainloop()