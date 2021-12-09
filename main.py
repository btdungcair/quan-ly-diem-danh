from tkinter import Menu, Tk
from views.login import LoginFrame
from views.menu import MenuFrame
from views.student_list import StudentListFrame
from views.face_recognition import FaceRecognitionFrame

window = Tk()
window.title("Quản lý điểm danh - HUS")
window.geometry("1280x720")
window.resizable(0, 0)
startFrame = MenuFrame(window)

# username: admin
# password: admin

if __name__ == "__main__":
    window.mainloop()