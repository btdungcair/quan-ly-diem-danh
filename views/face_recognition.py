from tkinter import *
from tkinter import filedialog
from views import base
from PIL import ImageTk, Image
from controller import *

class FaceRecognitionFrame(base.ParentFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=TOP, fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        super().create_widgets()
        self.import_image_button = Button(self, text="Import ảnh", font=("Arial", 18), bg="#F32463", fg="white", command=self.import_image)
        self.import_image_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def import_image(self):
        image_path_set = filedialog.askopenfilenames(title="Chọn ảnh", filetypes=(("Image Files", "*.jpg"), ("Image Files", "*.png"), ("Image Files", "*.jpeg"), ("All Files", "*.*")))
        for image_path in image_path_set:
            print(image_path)