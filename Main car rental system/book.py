from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('test.db')
print("CONNECTED!!!")

conn.execute("CREATE TABLE IF NOT EXISTS ENTRIES \
     (NAME  TEXT  PRIMARY KEY NOT NULL, \
     CONTACT INT NOT NULL, \
     SOURCE TEXT NOT NULL, \
     DESTINATION TEXT NOT NULL, \
     NOFDAYS INT);")
print("Table created successfully")

#conn.execute("CREATE TABLE IF NOT EXISTS car_available\
            #(car_name VARCHAR PRIMARY KEY ,\
            #mileage INT,\
           # model VARCHAR,\
           # available INT);")



print("CAR DETAILS ENTERED INTO TABLE ")
class book(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.f=Frame(root,height=1000,width=1200,bg='brown')
        self.f.propagate(0)
        self.f.pack()

        self.f1 = Frame(self.f, width=1200, height=250, bd=8,bg='sandybrown')
        self.f1.place(x=25, y=20,width=1150, height=250)
        self.f2 = Frame(self.f, width=1150, height=270, bd=8,bg='sandybrown')
        self.f2.place(x=25, y=300,width=1150, height=250)
        self.f3 = Frame(self.f, width=1150, height=100, bd=8,bg='sandybrown')
        self.f3.place(x=25, y=580,width=1150, height=100)

        lblCustomerName = Label(self.f1, font=('arial', 10, 'bold'), text='CUSTOMER NAME:', bd=8, fg='BLACK',
                                bg='sandybrown')
        lblCustomerName.place(x=350, y=50)
        self.txtCustomerName = Entry(self.f1, font=('arial', 10, 'bold'), width=31, justify='left')
        self.txtCustomerName.place(x=650, y=50)

        lblContactNo = Label(self.f1, font=('arial', 10, 'bold'), text='CONTACT NO.:', bd=8, fg='BLACK', bg='sandybrown')
        lblContactNo.place(x=350, y=120)
        self.txtContactNo = Entry(self.f1, font=('arial', 10, 'bold'),  width=31, justify='left')
        self.txtContactNo.place(x=650, y=120)

        self.var = StringVar(root)
        option = OptionMenu(self.f1, self.var, 'Honda', 'Mercedes', 'Mustang', 'Audi', 'Sedan', 'Mini',
                            'Chevrolt', 'Hyundai', 'Range Rover', 'Ferrari', 'peugeot', 'Lotus')
        # self.var.set('CAR')
        option.place(x=650, y=190)
        lbltype = Label(self.f1, font=('arial', 10, 'bold'), text='SELECT TYPE OF VEHICLE:', bd=4, fg='BLACK',
                        bg='sandybrown')
        lbltype.place(x=350, y=190)

        w = Message(self.f1, text="BOOK CAR ",
                    font=('calibri', 17, 'bold'), width=1000, fg='BLACK', bg='sandybrown')
        w.place(x=480,y=0)

        lblNoOfDaysRented = Label(self.f2, font=('arial', 10, 'bold'), text='NO. OF DAYS RENTED:', bd=8, fg='BLACK',
                                  bg='sandybrown')
        lblNoOfDaysRented.place(x=550, y=50)
        self.txtNoOfDaysRented = Entry(self.f2, font=('arial', 10, 'bold'),  width=31, justify='left')
        self.txtNoOfDaysRented.place(x=750, y=50)

        lblSource = Label(self.f2, font=('arial', 10, 'bold'), text='SOURCE:', bd=8, fg='BLACK', bg='sandybrown')
        lblSource.place(x=150, y=50)
        self.txtSource = Entry(self.f2, font=('arial', 10, 'bold'),  width=31, justify='left')
        self.txtSource.place(x=250, y=50)

        lblDestination = Label(self.f2, font=('arial', 10, 'bold'), text='DESTINATION:', bd=8, fg='BLACK', bg='sandybrown')
        lblDestination.place(x=120, y=150)
        self.txtDestination = Entry(self.f2, font=('arial', 10, 'bold'),  width=31, justify='left')
        self.txtDestination.place(x=250, y=150)

        lblTotal = Label(self.f2, font=('arial', 10, 'bold'), text='TOTAL:', bd=8, fg='BLACK', bg='sandybrown')
        lblTotal.place(x=650, y=150)
        self.txtTotal = Entry(self.f2, font=('arial', 10, 'bold'),  width=31, justify='left')
        self.txtTotal.place(x=750, y=150)

        btnTotal = Button(self.f3, text='TOTAL', padx=4, pady=4,  fg='black', bg='brown',
                          font=('arial', 12, 'bold'), width=14, height=1,command=self.rentalCost).place(x=200, y=20)

        btnBook = Button(self.f3, text='BOOK', padx=4, pady=4,  fg='black', bg='brown',
                         font=('arial', 12, 'bold'), width=14, height=1,command=self.book_car).place(x=500, y=20)

        btnExit = Button(self.f3, text='BACK', padx=4, pady=4,  fg='black', bg='Red',
                         font=('arial', 12, 'bold'), width=14, height=1,command=self.back).place(x=800, y=20)




    def back(self):
        import user
        self.f.destroy()
        user.User(self.master)

    def rentalCost(self):
        noOfDays = int(self.txtNoOfDaysRented.get())

        if self.var.get()=="Honda" or self.var.get()=="Sedan" or self.var.get()=="Mini" or self.var.get()=="Hyundai" or self.var.get()=="Range Rover":
                rent = noOfDays*800
        elif self.var.get()=="Mercedes" or self.var.get()=="Mustang":
                rent = noOfDays*1000
        elif self.var.get()=="Audi" or self.var.get()=="Ferrari":
                rent = noOfDays*2000
        elif self.var.get()=="peugeot" or self.var.get()=="Lotus":
                rent = noOfDays*2200
        else:
                rent = noOfDays*3000

        self.txtTotal.delete(0, tkinter.END)
        self.txtTotal.insert(0, rent)
        return


    def book_car(self):
        if self.txtCustomerName=='' or self.txtNoOfDaysRented=='' or self.txtSource=='' or self.txtDestination=='' or self.txtContactNo=='':
                tkinter.messagebox.showinfo("Error","PLEASE FILL ALL DETAILS BEFORE BOOKING")
        if self.var.get()=='':
                tkinter.messagebox.showinfo("Error","SELECT A VEHICLE BEFORE BOOKING")
        else:
            #print(str(self.var.get()))
            cursor = conn.execute("SELECT available FROM car_available WHERE car_name=?",(self.var.get(),))
            data = cursor.fetchone()
            r = int(data[0])
            if r == 1:
                self.rentalCost()
                conn.execute("UPDATE car_available SET available=0 WHERE car_name=?",(self.var.get(),))
                conn.commit()
                self.insert()
                tkinter.messagebox.showinfo("SUCCESSFUL", "BOOKING DONE")
            else:
                tkinter.messagebox.showinfo("VEHICLE NOT AVAILABLE", "TRY BOOKING LATER SELECTED VEHICLE IS NOT AVAILABLE")


    def insert(self):
        if self.txtCustomerName.get()=='' or self.txtContactNo.get()==0 or self.txtSource.get()=='' or self.txtDestination.get()=='' or self.txtNoOfDaysRented.get()==0 or self.var.get()=='':
            tkinter.messagebox.showinfo("Error", "Please Enter all the details")
            self.f.destroy()
            self.book_car()
        else:
            try:
                conn.execute("INSERT INTO ENTRIES (NAME,CONTACT,SOURCE,DESTINATION,NOFDAYS) \
                  VALUES (?,?,?,?,?)",(self.txtCustomerName.get(),self.txtContactNo.get(),self.txtSource.get(),self.txtDestination.get(),self.txtNoOfDaysRented.get(),))

                conn.commit()
            except sqlite3.IntegrityError:
                tkinter.messagebox.showinfo("Error", "The entered ID is already present")
            else:
                tkinter.messagebox.showinfo("BOOKED", "YOUR VEHICLE IS BOOKED!!")
                self.txtCustomerName.delete(0, END)
                self.txtContactNo.delete(0, END)
                self.txtSource.delete(0, END)
                self.txtDestination.delete(0, END)
                self.txtNoOfDaysRented.delete(0, END)
                self.txtTotal.delete(0, END)

