from tkinter import Tk
from view import *

window = Tk()
window.title("Test App")
window.geometry("700x400")
window.resizable(0, 0)
startFrame = MenuFrame(window)

if __name__ == "__main__":
    window.mainloop()