from tkinter import Tk
from views.login import LoginFrame
from views.student_list import StudentListFrame

window = Tk()
window.title("Test App")
window.geometry("700x400")
window.resizable(0, 0)
startFrame = StudentListFrame(window)

if __name__ == "__main__":
    window.mainloop()