from tkinter import *
from tkinter import messagebox
from views import menu
from PIL import ImageTk, Image
from controller import *

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=TOP, fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.canvas1 = Canvas(self, bg="#D1D1D1")
        self.canvas1.pack(side=TOP, fill="both", expand=True)

        self.canvas1.create_rectangle(200, 60, 600, 340, fill="#FFFFFF", outline="#B2B1B1")
        self.canvas1.create_rectangle(100, 90, 280, 310, fill="#573434", outline="#573434")#180x220
        self.hus_logo = ImageTk.PhotoImage(Image.open("images/huslogo.jpg"))
        self.canvas1.create_image(190, 200, image=self.hus_logo)

        self.canvas1.create_text(390, 100, text="Đăng nhập", font=("Arial", 20, "bold"), fill="#1160FB")

        self.canvas1.create_text(353, 150, text="Tài khoản", font=("Arial", 12))
        self.username_entry = Entry(self.canvas1, width=25, font=("Arial", 12), background="#C4C4C4")
        self.username_entry.place(x=320, y=170)

        self.canvas1.create_text(350, 220, text="Mật khẩu", font=("Arial", 12))
        self.password_entry = Entry(self.canvas1, width=25, font=("Arial", 12), background="#C4C4C4", show="*")
        self.password_entry.place(x=320, y=240)

        self.login_button = Button(self.canvas1, text="Đăng nhập", height=1, width=15, font=("Arial", 15), background="#F32463", foreground="white", command=self.login)
        self.login_button.place(x=345, y=285)

        self.master.bind("<Return>", self.login)

    def login(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if check_login(username, password):
            self.destroy()
            menu.MenuFrame(self.master).tkraise()
        else:
            messagebox.showerror("Thông báo", "Đăng nhập thất bại\nTài khoản hoặc mật khẩu không đúng.")