from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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
        super().create_widgets()
        self.attributes_set = ("STT", "Họ và tên", "Mã SV", "Ngày sinh", "Số tiết vắng")
        self.canvas1.create_text(150, 85, text="Tìm kiếm theo", font=("Arial", 12), fill="black")

        self.variable = StringVar(self.canvas1)
        self.variable.set("Thuộc tính")
        self.attribute_choosen = ttk.Combobox(self.canvas1, textvariable=self.variable, state="readonly", width=11)
        self.attribute_choosen["values"] = self.attributes_set
        self.attribute_choosen.current()
        self.attribute_choosen.place(x=220, y=75)

        self.value_entry = Entry(self.canvas1, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        self.value_entry.insert(0, "Nhập giá trị")
        self.value_entry.bind("<Button-1>", self.clear_entry)
        self.value_entry.place(x=340, y=75)

        self.search_button_icon = ImageTk.PhotoImage(Image.open("images/search.png"))
        self.search_button = Button(self.canvas1, image=self.search_button_icon, highlightthickness=0, bd=0, borderwidth=0)
        self.search_button.place(x=520, y=73)

        style = ttk.Style()
        style.theme_use("clam")

        self.table = ttk.Treeview(self.canvas1, height=10, show="headings", selectmode="browse")
        yscrollbar = ttk.Scrollbar(self.canvas1, orient=VERTICAL, command=self.table.yview)
        yscrollbar.place(x=630, y=100, height=230)
        self.table["columns"] = self.attributes_set
        self.table.column("STT", minwidth=50, width=50, anchor="center", stretch=NO)
        self.table.column("Họ và tên", minwidth=200, width=200, anchor="center", stretch=NO)
        self.table.column("Mã SV", minwidth=110, width=110, anchor="center", stretch=NO)
        self.table.column("Ngày sinh", minwidth=120, width=120, anchor="center", stretch=NO)
        self.table.column("Số tiết vắng", minwidth=100, width=100, anchor="center", stretch=NO)
        self.table.heading("STT", text="STT")
        self.table.heading("Họ và tên", text="Họ và tên")
        self.table.heading("Mã SV", text="Mã SV")
        self.table.heading("Ngày sinh", text="Ngày sinh")
        self.table.heading("Số tiết vắng", text="Số tiết vắng")
        self.table.place(x=50, y=100)
        self.insert_data()

        self.add_button = Button(self.canvas1, text="Thêm", width=8, font=("Arial", 11), bg="yellow", fg="black", command=self.add_student)
        self.add_button.place(x=210, y=340)
        self.modify_button = Button(self.canvas1, text="Sửa", width=8, font=("Arial", 11), bg="yellow", fg="black")
        self.modify_button.place(x=310, y=340)
        self.delete_button = Button(self.canvas1, text="Xóa", width=8, font=("Arial", 11), bg="yellow", fg="black")
        self.delete_button.place(x=410, y=340)

    def clear_entry(self, event):
        if self.value_entry.get() == "Nhập giá trị":
            self.value_entry.delete(0, END)

    def insert_data(self):
        student_list = sort_by_name(get_students_list())
        for i in range(len(student_list)):
            self.table.insert("", "end", values=(i+1, student_list[i][1], student_list[i][0], student_list[i][2], student_list[i][3]))

    def refresh_table(self):
        self.table.delete(*self.table.get_children())
        self.insert_data()

    def add_student(self):
        add_student_window = Toplevel(self.master)
        add_student_window.title("Thêm sinh viên")
        add_student_window.geometry("400x300+500+200")
        add_student_window.resizable(False, False)
        add_student_window.config(bg="#D1D1D1")
        add_student_window.grab_set()
        add_student_window.focus_set()

        fullname_label = Label(add_student_window, text="Họ và tên", font=("Arial", 11), bg="#D1D1D1")
        fullname_label.place(x=10, y=140)
        fullname_entry = Entry(add_student_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        fullname_entry.place(x=110, y=140)

        id_label = Label(add_student_window, text="Mã sinh viên", font=("Arial", 11), bg="#D1D1D1")
        id_label.place(x=10, y=180)
        id_entry = Entry(add_student_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        id_entry.place(x=110, y=180)

        dob_label = Label(add_student_window, text="Ngày sinh", font=("Arial", 11), bg="#D1D1D1")
        dob_label.place(x=10, y=220)
        dob_entry = Entry(add_student_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        dob_entry.place(x=110, y=220)

        absent_count_label = Label(add_student_window, text="Số tiết vắng", font=("Arial", 11), bg="#D1D1D1")
        absent_count_label.place(x=10, y=260)
        absent_count_entry = Entry(add_student_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        absent_count_entry.place(x=110, y=260)

        def add_student_to_db():
            fullname = fullname_entry.get()
            id = id_entry.get()
            dob = dob_entry.get()
            absent_count = absent_count_entry.get()
            if fullname == "" or id == "" or dob == "" or absent_count == "":
                messagebox.showinfo("Thông báo", "Hãy nhập đầy đủ thông tin")
            else:
                add_student(int(id), fullname, dob, int(absent_count))
                add_student_window.destroy()
                self.refresh_table()

        add_button = Button(add_student_window, text="Thêm", height=3, width=8, font=("Arial", 11), bg="yellow", fg="black", command=add_student_to_db)
        add_button.place(x=300, y=178)

class StatisticalFrame(ParentFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=TOP, fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        super().create_widgets()

        # columns = ['STT', 'Họ và tên', 'Mã sinh viên', 'Ngày sinh']

        self.canvas1.create_rectangle(50, 300, 650, 330, fill="#D1D1D1", outline="#D1D1D1")
        self.canvas1.create_text(360, 315, text="Tổng kết điểm danh sinh viên", font=("Arial", 15), fill="black")
        self.export_file_button = Button(self.canvas1, text="Xuất file", height=1, width=8, font=("Arial", 12), background="#E3C317", foreground="black")
        self.export_file_button.place(x=320, y=340)