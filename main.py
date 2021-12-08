from tkinter import Tk
from views.login import LoginFrame
from views.student_list import StudentListFrame

window = Tk()
window.title("Quản lý điểm danh - HUS")
# window.geometry("700x400")
window.geometry("1280x720")
window.resizable(0, 0)
startFrame = LoginFrame(window)

# username: admin
# password: admin

if __name__ == "__main__":
    window.mainloop()