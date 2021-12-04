from tkinter import *
from tkinter import messagebox
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
            MenuFrame(self.master).tkraise()
        else:
            messagebox.showerror("Thông báo", "Đăng nhập thất bại\nTài khoản hoặc mật khẩu không đúng.")

class ParentFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

    def create_widgets(self):
        self.canvas1 = Canvas(self, bg="#D1D1D1")
        self.canvas1.pack(side=TOP, fill="both", expand=True)

        self.background_image = ImageTk.PhotoImage(Image.open("images/background.png"))
        self.canvas1.create_image(30, 20, image=self.background_image, anchor=NW)

        self.back_icon = ImageTk.PhotoImage(Image.open("images/back.png"))
        self.back_button = Button(self.canvas1, image=self.back_icon, highlightthickness=0, bd=0, borderwidth=0, command=self.back)
        self.back_button.place(x=35, y=25)

        self.intro_image = ImageTk.PhotoImage(Image.open("images/intro.png"))
        self.canvas1.create_image(350, 50, image=self.intro_image)

        self.logout_icon = ImageTk.PhotoImage(Image.open("images/logout.png"))
        self.logout_button = Button(self.canvas1, image=self.logout_icon, highlightthickness=0, bd= 0, borderwidth=0, command=self.logout)
        self.logout_button.place(x=625, y=25)
    
    def back(self):
        previous_frame = None
        if type(self) is MenuFrame:
            self.logout()
        else:
            previous_frame = MenuFrame(self.master)
        if not previous_frame is None:
            self.destroy()
            previous_frame.tkraise()

    def logout(self):
        msgbox = messagebox.askyesno("Thông báo", "Bạn có chắc chắn muốn đăng xuất?")
        if msgbox:
            login_frame = LoginFrame(self.master)
            self.destroy()
            login_frame.tkraise()
        else:
            return

class MenuFrame(ParentFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=TOP, fill="both", expand=True)      
        self.create_widgets()
    
    def create_widgets(self):
        super().create_widgets()
        self.student_button_icon = ImageTk.PhotoImage(Image.open("images/button_sinhvien.png"))
        self.student_button = Button(self.canvas1, image=self.student_button_icon, highlightthickness=0, bd=0, borderwidth=0, command=lambda: self.switch_frame("student_frame"))
        self.student_button.place(x=60, y=180)

        self.face_recognition_button_icon = ImageTk.PhotoImage(Image.open("images/button_nhandien.png"))
        self.face_recognition_button = Button(self.canvas1, image=self.face_recognition_button_icon, highlightthickness=0, bd=0, borderwidth=0, command=lambda: self.switch_frame("face_recognition_frame"))
        self.face_recognition_button.place(x=210, y=180)

        self.attendance_button_icon = ImageTk.PhotoImage(Image.open("images/button_diemdanh.png"))
        self.attendance_button = Button(self.canvas1, image=self.attendance_button_icon, highlightthickness=0, bd=0, borderwidth=0, command=lambda: self.switch_frame("attendance_frame"))
        self.attendance_button.place(x=360, y=180)

        self.statistical_button_icon = ImageTk.PhotoImage(Image.open("images/button_thongke.png"))
        self.statistical_button = Button(self.canvas1, image=self.statistical_button_icon, highlightthickness=0, bd=0, borderwidth=0, command=lambda: self.switch_frame("statistical_frame"))
        self.statistical_button.place(x=510, y=180)

    def switch_frame(self, frame_name):
        if frame_name == "statistical_frame":
            self.destroy()
            StatisticalFrame(self.master).tkraise()
        elif frame_name == "student_frame":
            self.destroy()
            StudentFrame(self.master).tkraise()
        else:
            return

class StudentFrame(ParentFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=TOP, fill="both", expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        return super().create_widgets()

class StatisticalFrame(ParentFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=TOP, fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        super().create_widgets()

        columns = ['STT', 'Họ và tên', 'Mã sinh viên', 'Ngày sinh']

        self.canvas1.create_rectangle(50, 300, 650, 330, fill="#D1D1D1", outline="#D1D1D1")
        self.canvas1.create_text(360, 315, text="Tổng kết điểm danh sinh viên", font=("Arial", 15), fill="black")
        self.export_file_button = Button(self.canvas1, text="Xuất file", height=1, width=8, font=("Arial", 12), background="#E3C317", foreground="black")
        self.export_file_button.place(x=320, y=340)