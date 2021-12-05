from tkinter import *
from views import base, statistical, student_list
from PIL import ImageTk, Image
from controller import *

class MenuFrame(base.ParentFrame):
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
            statistical.StatisticalFrame(self.master).tkraise()
        elif frame_name == "student_frame":
            self.destroy()
            student_list.StudentListFrame(self.master).tkraise()
        else:
            return