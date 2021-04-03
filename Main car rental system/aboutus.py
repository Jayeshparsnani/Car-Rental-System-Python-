
from tkinter import *
import sys
from PIL import ImageTk,Image


class AboutUs(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.f =Frame(root, height=1000, width=1200,bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()

        l1 = Label(self.f, text="ABOUT US", height=2, width=66, font=('bold', 12),bg='sandybrown')
        l1.place(x=300, y=4)
        l2 = Label(self.f, text="INFORMATION:", height=2, font=('bold', 12),bg='sandybrown')
        l2.place(x=100, y=250)
        self.m1 = Message(self.f, text= 'Economy Is Our First Name One of our top priorities is to adjust each package we offer to our customer’s exact needs. We offer a variety of options that can enhance your experience, Always according to your necessities, and help you get the best out of your holidays or your business trip.', font=('bold',12),fg='black',bg='sandybrown')
        self.m1.place(x=100,y=300)
        self.m2=Message(self.f,text='Leading Experts EconomyCarRentals has provided millions of customers with the best possible guaranteed price for their Car Rental.We welcome you to become our next satisfied customer.', font=('bold',12),fg='black',bg='sandybrown')
        self.m2.place(x=800,y=300)
        self.m3=Message(self.f,text='Book Safe And Easy Our smart booking engine searches for for the best price, car category, extras, exclusive offers and discounts suiting your needs.You can securely book online today only with a small downpayment and pay the rest upon your arrival at the desk!', font=('bold',12),fg='black',bg='sandybrown')
        self.m3.place(x=450, y=300)

        b1 = Button(self.f, text='HOME', height=2, width=20,command=self.home,activebackground='gray',activeforeground='red',bg='red')
        b1.place(x=900, y=600)

        c = Canvas(root, bg='sandybrown', height=150, width=150,highlightbackground="sandybrown")
        c.create_oval(150, 150, 4, 5, width=2, fill="BLACK", outline="red")

        fnt = ('times', 15, 'bold italic')

        id = c.create_text(80, 80, text="  DDJS \nCAR RENTAL", font=fnt, fill="red", activefill="green")

        c.place(x=520,y=50)

        
    def home(self):
        import home
        self.f.destroy()
        home.Home(self.master)
