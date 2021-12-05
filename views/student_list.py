from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from views import base, student_info
from PIL import ImageTk, Image
from controller import *

class StudentListFrame(base.ParentFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=TOP, fill="both", expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        super().create_widgets()
        self.attributes_set = ("STT", "Họ và tên", "Mã SV", "GT", "Ngày sinh", "Số tiết vắng")
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
        self.search_button = Button(self.canvas1, image=self.search_button_icon, highlightthickness=0, bd=0, borderwidth=0, command=self.search)
        self.search_button.place(x=520, y=73)

        style = ttk.Style()
        style.theme_use("clam")

        self.table = ttk.Treeview(self.canvas1, height=10, show="headings", selectmode="browse")
        yscrollbar = ttk.Scrollbar(self.canvas1, orient=VERTICAL, command=self.table.yview)
        yscrollbar.place(x=630, y=100, height=230)
        self.table["columns"] = self.attributes_set
        self.table.column("STT", minwidth=50, width=50, anchor="center", stretch=NO)
        self.table.column("Họ và tên", minwidth=200, width=200, anchor="center", stretch=NO)
        self.table.column("Mã SV", minwidth=100, width=100, anchor="center", stretch=NO)
        self.table.column("GT", minwidth=50, width=50, anchor="center", stretch=NO)
        self.table.column("Ngày sinh", minwidth=100, width=100, anchor="center", stretch=NO)
        self.table.column("Số tiết vắng", minwidth=80, width=80, anchor="center", stretch=NO)
        self.table.heading("STT", text="STT")
        self.table.heading("Họ và tên", text="Họ và tên")
        self.table.heading("Mã SV", text="Mã SV")
        self.table.heading("GT", text="GT")
        self.table.heading("Ngày sinh", text="Ngày sinh")
        self.table.heading("Số tiết vắng", text="Số tiết vắng")
        self.table.place(x=50, y=100)
        self.insert_data()

        self.table.bind("<Double-1>", self.show_student_info)

        self.add_button = Button(self.canvas1, text="Thêm", width=8, font=("Arial", 11), bg="yellow", fg="black", command=self.open_add_student_window)
        self.add_button.place(x=210, y=340)
        self.modify_button = Button(self.canvas1, text="Sửa", width=8, font=("Arial", 11), bg="yellow", fg="black", command=self.open_modify_student_window)
        self.modify_button.place(x=310, y=340)
        self.delete_button = Button(self.canvas1, text="Xóa", width=8, font=("Arial", 11), bg="yellow", fg="black", command=self.remove_student)
        self.delete_button.place(x=410, y=340)

    def clear_entry(self, event):
        if self.value_entry.get() == "Nhập giá trị":
            self.value_entry.delete(0, END)

    def search(self):
        attribute = self.attribute_choosen.current()
        value = self.value_entry.get()
        selections = []
        if not attribute == "Thuộc tính" and not len(value) == 0:
            for child in self.table.get_children():
                if value.lower() in str(self.table.item(child)['values'][attribute]).lower():
                    selections.append(child)
            self.table.selection_set(selections)
            print(selections)

    def insert_data(self):
        student_list = sort_by_name(get_students_list())
        for i in range(len(student_list)):
            self.table.insert("", "end", values=(i+1, student_list[i][1], student_list[i][0], student_list[i][2], student_list[i][3], student_list[i][4]))

    def refresh_table(self):
        self.table.delete(*self.table.get_children())
        self.insert_data()

    def selected_student(self):
        selected = self.table.focus()
        values = self.table.item(selected, "values")
        return values

    def remove_student(self):
        student = self.selected_student()
        if student:
            if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa sinh viên này?"):
                delete_student(student[2])
                self.refresh_table()
        else:
            messagebox.showinfo("Thông báo", "Chưa chọn sinh viên nào")
        

    def create_new_window(self, title):
        self.new_window = Toplevel(self.master)
        self.new_window.title(title)
        self.new_window.geometry("400x300+500+200")
        self.new_window.resizable(False, False)
        self.new_window.config(bg="#D1D1D1")
        self.new_window.grab_set()
        self.new_window.focus_set()

        self.fullname_label = Label(self.new_window, text="Họ và tên", font=("Arial", 11), bg="#D1D1D1")
        self.fullname_label.place(x=10, y=140)
        self.fullname_entry = Entry(self.new_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        self.fullname_entry.place(x=110, y=140)

        self.id_label = Label(self.new_window, text="Mã sinh viên", font=("Arial", 11), bg="#D1D1D1")
        self.id_label.place(x=10, y=170)
        self.id_entry = Entry(self.new_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        self.id_entry.place(x=110, y=170)

        self.gender_label = Label(self.new_window, text="Giới tính", font=("Arial", 11), bg="#D1D1D1")
        self.gender_label.place(x=10, y=200)
        self.gender_entry = Entry(self.new_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        self.gender_entry.place(x=110, y=200)

        self.dob_label = Label(self.new_window, text="Ngày sinh", font=("Arial", 11), bg="#D1D1D1")
        self.dob_label.place(x=10, y=230)
        self.dob_entry = Entry(self.new_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        self.dob_entry.place(x=110, y=230)

        self.absent_count_label = Label(self.new_window, text="Số tiết vắng", font=("Arial", 11), bg="#D1D1D1")
        self.absent_count_label.place(x=10, y=260)
        self.absent_count_entry = Entry(self.new_window, width=20, font=("Arial", 11), highlightbackground="black", highlightthickness=1, borderwidth=0)
        self.absent_count_entry.place(x=110, y=260)

    def open_add_student_window(self):
        self.create_new_window("Thêm sinh viên")
        def _add_student():
            fullname = self.fullname_entry.get()
            id = self.id_entry.get()
            dob = self.dob_entry.get()
            absent_count = self.absent_count_entry.get()
            if fullname == "" or id == "" or dob == "" or absent_count == "":
                messagebox.showinfo("Thông báo", "Hãy nhập đầy đủ thông tin")
            elif not valid_id(id):
                messagebox.showinfo("Thông báo", "Mã sinh viên không hợp lệ hoặc đã tồn tại")
            else:
                add_student(int(id), fullname, dob, int(absent_count))
                self.new_window.destroy()
                self.refresh_table()

        add_button = Button(self.new_window, text="Thêm", height=3, width=8, font=("Arial", 11), bg="yellow", fg="black", command=_add_student)
        add_button.place(x=300, y=178)
    
    def open_modify_student_window(self):
        student = self.selected_student()
        if len(student) == 0:
            messagebox.showinfo("Thông báo", "Hãy chọn sinh viên cần sửa")
        else:
            self.create_new_window("Sửa sinh viên")
            self.fullname_entry.insert(0, student[1])
            self.id_entry.insert(0, student[2])
            self.gender_entry.insert(0, student[3])
            self.dob_entry.insert(0, student[4])
            self.absent_count_entry.insert(0, student[5])

            def _modify_student():
                fullname = self.fullname_entry.get()
                id = self.id_entry.get()
                dob = self.dob_entry.get()
                absent_count = self.absent_count_entry.get()
                if fullname == "" or id == "" or dob == "" or absent_count == "":
                    messagebox.showinfo("Thông báo", "Hãy nhập đầy đủ thông tin")
                elif not valid_id(id):
                    messagebox.showinfo("Thông báo", "Mã sinh viên không hợp lệ hoặc đã tồn tại")
                else:
                    update_student(int(id), fullname, dob, int(absent_count))
                    self.new_window.destroy()
                    self.refresh_table()

            modify_button = Button(self.new_window, text="Sửa", height=3, width=8, font=("Arial", 11), bg="yellow", fg="black", command=_modify_student)
            modify_button.place(x=300, y=178)

    def show_student_info(self, event):
        student = self.selected_student()
        self.destroy()
        student_info.StudentInfoFrame(self.master, student).tkraise()