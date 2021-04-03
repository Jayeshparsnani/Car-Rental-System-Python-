from tkinter import *
import tkinter.messagebox
import sqlite3
conn=sqlite3.connect('test.db')
print("CONNECTED!!!")

conn.execute("CREATE TABLE IF NOT EXISTS car_available(car_name VARCHAR PRIMARY KEY,mileage INT,model VARCHAR,available INT)")


class Add(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.f=Frame(root,height=1000,width=1200,bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()

        self.l0 = Label(self.f, text="ADD CAR", bg='sandybrown', font=("bold", 20))
        self.l1 = Label(self.f, text="Car Name:", bg='sandybrown')
        self.l2 = Label(self.f, text="Mileage:", bg='sandybrown')
        self.l3 = Label(self.f, text="Model No.:", bg='sandybrown')
        self.l4 = Label(self.f, text="Availability:", bg='sandybrown')

        self.e1 = Entry(self.f, width=25, bg="white",fg="black")
        self.e2 = Entry(self.f, width=25, bg="white", fg="black")
        self.e3 = Entry(self.f, width=40, bg="white", fg="black")
        self.e4 = Entry(self.f, width=25, bg="white", fg="black")

        self.l0.place(x=520, y=120)
        self.l1.place(x=420, y=190)
        self.l2.place(x=420, y=240)
        self.l3.place(x=420, y=290)
        self.l4.place(x=420, y=340)

        self.e1.place(x=600, y=190, height=25, width=200)
        self.e2.place(x=600, y=240, height=25, width=200)
        self.e3.place(x=600, y=290, height=25, width=200)
        self.e4.place(x=600, y=340, height=25, width=200)

        self.b = Button(self.f, text="Add Car", width="20", height="2", command=self.add,
                        activebackground='gray', activeforeground='red', bg='brown')

        self.b.place(x=400, y=450)
        b1 = Button(self.f, text='Back', height=2, width=20, command=self.back, activebackground='gray',
                    activeforeground='red', bg='red')
        b1.place(x=700, y=450)

    def add(self):
        carname = self.e1.get()
        Mileage= self.e2.get()
        Model= self.e3.get()
        Avail= self.e4.get()

        if carname == "" or Mileage == "" or Model == "" or Avail == "":
            tkinter.messagebox.showinfo("Error", "PLEASE FILL ALL THE CREDENTIALS")

        else:

            try:
                conn.execute("UPDATE car_available SET available=1 WHERE car_name=?", (self.e1.get(),))
                conn.commit()

            except sqlite3.IntegrityError:
                tkinter.messagebox.showinfo("Error", "The entered car is already present")
            else:
                tkinter.messagebox.showinfo("SUCCESSFUL", "CAR ADDED")
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e3.delete(0, END)
                self.e4.delete(0, END)

    def back(self):
        import adminlog
        self.f.destroy()
        adminlog.Admin(self.master)