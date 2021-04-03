from tkinter import *

import tkinter.messagebox
import sqlite3
conn=sqlite3.connect('test.db')
print("CONNECTED!!!")

conn.execute("CREATE TABLE IF NOT EXISTS car_available\
            (car_name VARCHAR PRIMARY KEY,\
            mileage INT,\
            model VARCHAR,\
            available INT);")



class Delete(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.f = Frame(root, height=1000, width=1200,bg='sandy brown')
        self.f.propagate(0)
        self.f.pack()

        self.l0 = Label(self.f, text="DELETE CAR",font=("Arial", 20),bg='sandy brown')
        self.l1 = Label(self.f, text="carname:",font=("Arial", 18),bg='sandy brown')


        self.e1 = Entry(self.f, width=25, bg="white", fg="black", font=("Arial", 14))


        self.l0.place(x=510, y=200)
        self.l1.place(x=420, y=280)


        self.e1.place(x=550, y=280)


        self.b = Button(self.f, text="Delete", width="20", height="2", activebackground='gray',
                        activeforeground='red', bg='brown',command=self.checkcarname)

        self.b.place(x=450, y=400)
        b1 = Button(self.f, text='Back', height=2, width=20, bg='red',command=self.back)
        b1.place(x=700, y=400)

    def checkcarname(self):
        name = self.e1.get()

        if name == "":
            tkinter.messagebox.showinfo("Error", "PLEASE FILL ALL THE CREDENTIALS")

        else:

            try:
                conn.execute("UPDATE car_available SET available=-1 WHERE car_name=?", (name,))
                conn.commit()

                conn.commit()
            except sqlite3.IntegrityError:
                tkinter.messagebox.showinfo("Error", "CANNOT BE DELETED")

            else:
                tkinter.messagebox.showinfo("DELETED", "CAR DELETED!!")
                self.e1.delete(0, END)



    def back(self):
        import adminlog
        self.f.destroy()
        adminlog.Admin(self.master)
