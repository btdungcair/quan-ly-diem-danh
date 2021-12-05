from tkinter import *
from views import base, student_list
from PIL import ImageTk, Image
from controller import *

class StudentInfoFrame(base.ParentFrame):
    def __init__(self, master, student=None):
        super().__init__(master)
        self.student = student
        self.pack(side=TOP, fill=BOTH, expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        super().create_widgets()
        self.canvas1.create_rectangle(40, 120, 200, 320, fill='black')
        self.fullname_label = Label(self.canvas1, text=self.student[1], font=('Arial', 15), fg="white", bg="#F32463")
        self.fullname_label.place(x=250, y=120)

        self.id_label = Label(self.canvas1, text="Mã sinh viên: "+self.student[2], font=('Arial', 15), fg="black")
        self.id_label.place(x=245, y=160)

        self.gender_label = Label(self.canvas1, text="Giới tính: "+self.student[3], font=('Arial', 15), fg="black")
        self.gender_label.place(x=245, y=200)

        self.gender_label = Label(self.canvas1, text="Ngày sinh: "+self.student[4], font=('Arial', 15), fg="black")
        self.gender_label.place(x=245, y=240)

        self.gender_label = Label(self.canvas1, text="Số buổi vắng: "+self.student[5], font=('Arial', 15), fg="black")
        self.gender_label.place(x=245, y=280)

    def back(self):
        self.destroy()
        student_list.StudentListFrame(self.master).tkraise()