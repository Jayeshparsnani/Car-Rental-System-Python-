from tkinter import *
#install package pillow-settings
#1.project ke andr jaa
#2.project interpretur
#3.search pillow and install
from PIL import ImageTk,Image #python image library
from tkinter import messagebox


class DefaultPage():
    def __init__(self,root): #1.add frame 2.add image 3.add text
        self.root=root
        self.f=Frame(self.root,width=1440,height=400)
        self.f.pack()

        self.img=ImageTk.PhotoImage(Image.open('123.png'))
        self.panel=Label(self.f,image=self.img)
        self.panel.pack()
        self.m=Message(self.f,width=600,font='Roman 20 bold italic',text='DDJS CARRENTAL',bg='red',relief=RAISED,borderwidth=4)
        self.m.place(x=20, y=25)
        self.panel.pack_propagate(0)
        self.f.pack_propagate(0)



#root=Tk()
#c=DefaultPage(root)
#root.mainloop()