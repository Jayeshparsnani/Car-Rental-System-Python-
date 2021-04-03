from tkinter import *
import sqlite3
conn=sqlite3.connect('test.db')
print("CONNECTED!!!")

class display(Frame):
    def __init__(self, root):

        Frame.__init__(self)
        self.f = Frame(root, height=1000, width=1200, bg='brown')
        self.f.propagate(0)
        self.f.pack()


        print("Details:")

        # winddisplay = Tk()
        # winddisplay.title("DISPLAY")
        # self.f.geometry('1300x700+100+50')
        label1 = Label(self.master)
        label1.config(text="NAME:", width=20, bg='ivory1', fg='royalblue')
        label1.place(x=100, y=100)

        label2 = Label(self.master)
        label2.config(text="CONTACT NO.", width=20, bg='ivory1', fg='royalblue')
        label2.place(x=250, y=100)

        label3 = Label(self.master)
        label3.config(text="SOURCE", width=20, bg='ivory1', fg='royalblue')
        label3.place(x=380, y=100)

        label4 = Label(self.master)
        label4.config(text="DESTINATION", width=20, bg='ivory1', fg='royalblue')
        label4.place(x=480, y=100)

        label5 = Label(self.master)
        label5.config(text="NO. OF DAYS", width=20, bg='ivory1', fg='royalblue')
        label5.place(x=600, y=100)

        cursor = conn.execute("SELECT NAME,CONTACT,SOURCE,DESTINATION,NOFDAYS from ENTRIES")
        data = cursor.fetchall()
        # print("NAME\t    CONTACT\t  SOURCE\t  DESTINATION\t  \tNOFDAYS")

        ax = 125
        for row in data:
            text1 = Label(self.master)
            text1.config(text=str(row[0]), width=20, bg='lavenderblush1', fg='hotpink', padx=5)
            text1.place(x=100, y=ax)

            text2 = Label(self.master)
            text2.config(text=row[1], width=20, bg='lavenderblush1', fg='hotpink', padx=5)
            text2.place(x=250, y=ax)

            text3 = Label(self.master)
            text3.config(text=str(row[2]), width=20, bg='lavenderblush1', fg='hotpink', padx=5)
            text3.place(x=380, y=ax)

            text4 = Label(self.master)
            text4.config(text=str(row[3]), width=20, bg='lavenderblush1', fg='hotpink', padx=5)
            text4.place(x=480, y=ax)

            text5 = Label(self.master)
            text5.config(text=row[4], width=20, bg='lavenderblush1', fg='hotpink', padx=5)
            text5.place(x=600, y=ax)

            ax = ax + 25

            b1 = Button(self.f, text='BACK', height=2, width=20, command=self.back, activebackground='gray',
                        activeforeground='red', bg='red')
            b1.place(x=900, y=600)

    def back(self):
        import adminlog
        self.f.destroy()
        adminlog.Admin(self.master)