from tkinter import *
from defaultpage import *

class MainPage(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.add_widgets()

    def test(self,login_type):

        print(f"test called {login_type}")



    def add_widgets(self):
        self.admin_button=Button(self.panel,text='Admin login',width=20,height=2,bg='sandybrown',activebackground='gray',activeforegroun='red',command=self.admin)
        self.admin_button.place(x=350,y=150)
        self.user_button = Button(self.panel, text='User login', width=20, height=2,bg='sandybrown', activebackground='gray',command=lambda:self.test("User"))
        self.user_button.place(x=550, y=150)
        self.new_user_button = Button(self.panel, text='New user?Sign up here',bg='sandybrown', width=20, height=2, activebackground='gray',borderwidth=2,relief=RIDGE)
        self.new_user_button .place(x=450, y=220)


    def admin(self):
        import adminlogin
        self.f.destroy()
        adminlogin.Adminlogin(self.root)



root=Tk()
m=MainPage(root)
root.mainloop()