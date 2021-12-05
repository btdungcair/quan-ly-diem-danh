from tkinter import *
from tkinter import messagebox
from views import base
from PIL import ImageTk, Image
from controller import *

class StatisticalFrame(base.ParentFrame):
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