from tkinter import *
import sys
from PIL import ImageTk,Image
from tkinter import Tk, Label, PhotoImage


class Home(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.f = Frame(root, height=1000, width=1200,bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()
        self.master = root

        l1 = Label(self.f, text="DDJS CAR RENTALS", fg='red', height=2, width=66, font=('bold', 12),bg='black')
        l1.place(x=0, y=4)

        b1 = Button(self.f, text='Login', height=2, width=20, command=self.login,activebackground='gray',activeforeground='red',bg='brown')
        b2 = Button(self.f, text='Register', height=2, width=20, command=self.register,activebackground='gray',activeforeground='red',bg='brown')
        b3 = Button(self.f, text='About Us', height=2, width=20, command=self.about,activebackground='gray',activeforeground='red',bg='brown')
        b4 = Button(self.f, text='Cars', height=2, width=20,command=self.car,activebackground='gray',activeforeground='red',bg='brown')
        b1.place(x=600, y=4)
        b2.place(x=750, y=4)
        b3.place(x=1050, y=4)
        b4.place(x=900, y=4)

        img = PhotoImage(file='5.png')
        my_image = Label(root, image=img, height=500, width=1000,bg='sandybrown')
        my_image.image=img
        my_image.place(x=150, y=200)

    def register(self):
        import register
        self.f.destroy()
        register.Register(self.master)

    def login(self):
        import adminuser
        self.f.destroy()
        adminuser.switch(self.master)

    def about(self):
        import aboutus
        self.f.destroy()
        aboutus.AboutUs(self.master)

    def car(self):
        import cars
        self.f.destroy()
        cars.Cars(self.master)

