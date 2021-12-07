from tkinter import *
from views.base import ParentFrame
from views import student_list
from PIL import ImageTk, Image
from controller import *

class StudentInfoFrame(ParentFrame):
    def __init__(self, master, student=None):
        super().__init__(master)
        self.student = student
        self.pack(side=TOP, fill=BOTH, expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        super().create_widgets()

        self.canvas1.create_rectangle(39, 119, 200, 320, fill='red', outline='red')

        try:
            image = Image.open("student_images/{}.jpg".format(self.student.get_id()))
        except:
            image = Image.open("student_images/{}.png".format(self.student.get_id()))

        image = image.resize((160, 200), Image.ANTIALIAS)
        self.student_image = ImageTk.PhotoImage(image)
        self.canvas1.create_image(120, 220, image=self.student_image)

        self.fullname_label = Label(self.canvas1, text=self.student.get_fullname(), font=('Arial', 15), fg="white", bg="#F32463")
        self.fullname_label.place(x=250, y=120)

        self.id_label = Label(self.canvas1, text="Mã sinh viên: "+self.student.get_id(), font=('Arial', 15), fg="black")
        self.id_label.place(x=245, y=160)

        self.gender_label = Label(self.canvas1, text="Giới tính: "+self.student.get_gender(), font=('Arial', 15), fg="black")
        self.gender_label.place(x=245, y=200)

        self.gender_label = Label(self.canvas1, text="Ngày sinh: "+self.student.get_dob(), font=('Arial', 15), fg="black")
        self.gender_label.place(x=245, y=240)

        self.gender_label = Label(self.canvas1, text="Số buổi vắng: "+self.student.get_absent_count(), font=('Arial', 15), fg="black")
        self.gender_label.place(x=245, y=280)

    def back(self):
        self.destroy()
        student_list.StudentListFrame(self.master).tkraise()