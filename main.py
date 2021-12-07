from tkinter import Tk
from views.login import LoginFrame

window = Tk()
window.title("Quản lý điểm danh - HUS")
window.geometry("700x400")
window.resizable(0, 0)
startFrame = LoginFrame(window)

# username: admin
# password: admin

if __name__ == "__main__":
    window.mainloop()