from tkinter import *
import sqlite3
conn = sqlite3.connect('test.db')
print("CONNECTED!!!")


class Return(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.f = Frame(root, height=1000, width=1200, bd=8, relief="raise", bg="sandybrown")
        self.f.propagate(0)
        self.f.pack()
        self.v = IntVar()
        cursor = conn.execute("SELECT car_name FROM car_available WHERE available=?", (0,))  # currently unavailable
        data = cursor.fetchall()


        ax = 50
        #m = 1
        self.lst_radios=[]
        for i in data:
            ans = str(i[0])
            choose=Radiobutton(self.f, text=ans, padx=20, variable=self.v, font=('arial', 12, 'bold'), value=len(self.lst_radios))
            self.lst_radios.append(ans)
            choose.pack(anchor=W)
         #   m = m + 1
        print(self.lst_radios)

        btnok = Button(self.f, text='OK', padx=4, pady=4, fg='black', bg='brown',
                       font=('arial', 12, 'bold'), width=14, height=1, command=self.make_available)
        btnok.place(x=450, y=500)

        btnok1 = Button(self.f, text='BACK', padx=4, pady=4, fg='black', bg='brown',
                       font=('arial', 12, 'bold'), width=14, height=1, command=self.back)
        btnok1.place(x=650, y=500)


    def make_available(self):
        print("INside make available fn")
        value=self.v.get()
        print("Value is ",value)
        ans=self.lst_radios[value]
        print("ans is ",ans)
        conn.execute("UPDATE car_available SET available=1 WHERE car_name=?", (ans,))
        conn.commit()
#        self.choose.pack_forget()
        import user
        self.f.destroy()
        user.User(self.master)

    def back(self):
        import user
        self.f.destroy()
        user.User(self.master)
