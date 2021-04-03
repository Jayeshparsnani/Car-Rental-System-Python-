from tkinter import *
import tkinter.messagebox

class Cars(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.f=Frame(root,height=1000,width=1200,bg='sandybrown')
        self.f.propagate(0)
        self.f.pack()

        img1 = PhotoImage(file='h.png')
        img2 = PhotoImage(file='m.png')
        img3 = PhotoImage(file='mu.png')
        img4 = PhotoImage(file='a.png')
        img5 = PhotoImage(file='z.png')
        img6 = PhotoImage(file='x.png')
        img7 = PhotoImage(file='c.png')
        img8 = PhotoImage(file='v.png')
        img9 = PhotoImage(file='b.png')
        img10 = PhotoImage(file='u.png')
        img11 = PhotoImage(file='y.png')
        img12 = PhotoImage(file='o.png')



        self.l0 = Label(self.f, text="CARS PROVIDED BY US", height=2, width=66,bg='sandybrown', font=('bold', 20))

        self.l1 = Label(self.f,image=img1, height=100, width=100 , bg='white')
        self.l1.image = img1
        self.l2 = Label(self.f,image=img2, height=100, width=100, bg='white')
        self.l2.image = img2
        self.l3 = Label(self.f,image=img3 , height=100, width=100, bg='white')
        self.l3.image = img3
        self.l4 = Label(self.f,image=img4, height=100, width=100, bg='white')
        self.l4.image = img4
        self.l5 = Label(self.f,image=img5, height=100, width=100, bg='white')
        self.l5.image = img5
        self.l6 = Label(self.f,image=img6 , height=100, width=100, bg='white')
        self.l6.image = img6
        self.l7 = Label(self.f, image=img7, height=100, width=100, bg='white')
        self.l7.image = img7
        self.l8 = Label(self.f, image=img8, height=100, width=100, bg='white')
        self.l8.image = img8
        self.l9 = Label(self.f, image=img9, height=100, width=100, bg='white')
        self.l9.image = img9
        self.l10 = Label(self.f, image=img10, height=100, width=100, bg='white')
        self.l10.image = img10
        self.l11 = Label(self.f, image=img11, height=100, width=100, bg='white')
        self.l11.image = img11
        self.l12 = Label(self.f, image=img12, height=100, width=100, bg='black')
        self.l12.image = img12

        self.l1.bind("<Button-1>", lambda e: self.car1())
        self.l2.bind("<Button-1>", lambda e: self.car2())
        self.l3.bind("<Button-1>", lambda e: self.car3())
        self.l4.bind("<Button-1>", lambda e: self.car4())
        self.l5.bind("<Button-1>", lambda e: self.car5())
        self.l6.bind("<Button-1>", lambda e: self.car6())

        self.l7.bind("<Button-1>", lambda e: self.car7())

        self.l8.bind("<Button-1>", lambda e: self.car8())

        self.l9.bind("<Button-1>", lambda e: self.car9())

        self.l10.bind("<Button-1>", lambda e: self.car10())

        self.l11.bind("<Button-1>", lambda e: self.car11())

        self.l12.bind("<Button-1>", lambda e: self.car12())






        self.l0.place(x=80, y=40)
        self.l1.place(x=180, y=150)
        self.l2.place(x=180, y=300)
        self.l3.place(x=180, y=450)
        self.l4.place(x=430, y=150)
        self.l5.place(x=430, y=300)
        self.l6.place(x=430, y=450)
        self.l7.place(x=670, y=150)
        self.l8.place(x=670, y=300)
        self.l9.place(x=670, y=450)
        self.l10.place(x=920, y=150)
        self.l11.place(x=920, y=300)
        self.l12.place(x=920, y=450)

        b1 = Button(self.f, text='HOME', height=2, width=20, command=self.home, activebackground='gray',
                    activeforeground='red', bg='red')
        b1.place(x=900, y=600)


    def car1(self):
        tkinter.messagebox.showinfo("car", "Name:Honda\nMileage:100\nModel:A\nAvailable:1")

    def car2(self):
        tkinter.messagebox.showinfo("car", "Name:Mercedes\nMileage:200\nModel:B\nAvailable:1")
    def car3(self):
        tkinter.messagebox.showinfo("car", "Name:Mustang\nMileage:300\nModel:C\nAvailable:1")
    def car4(self):
        tkinter.messagebox.showinfo("car", "Name:Audi\nMileage:400\nModel:D\nAvailable:1")
    def car5(self):
        tkinter.messagebox.showinfo("car", "Name:Sedan\nMileage:500\nModel:M\nAvailable:1")
    def car6(self):
        tkinter.messagebox.showinfo("car", "Name:Mini\nMileage:400\nModel:N\nAvailable:1")
    def car7(self):
        tkinter.messagebox.showinfo("car", "Name:Chevrolt\nMileage:300\nModel:K\nAvailable:1")
    def car8(self):
        tkinter.messagebox.showinfo("car", "Name:Hyundai\nMileage:200\nModel:J\nAvailable:1")
    def car9(self):
        tkinter.messagebox.showinfo("car", "Name:Range Rover\nMileage:200\nModel:F\nAvailable:1")
    def car10(self):
        tkinter.messagebox.showinfo("car", "Name:Ferrari\nMileage:100\nModel:R\nAvailable:1")
    def car11(self):
        tkinter.messagebox.showinfo("car", "Name:peugeot\nMileage:800\nModel:T\nAvailable:1")

    def car12(self):
        tkinter.messagebox.showinfo("car", "Name:Lotus\nMileage:200\nModel:A\nAvailable:1")

    def home(self):
        import home
        self.f.destroy()
        home.Home(self.master)



