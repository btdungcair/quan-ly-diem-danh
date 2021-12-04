
import sys
     
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    
    
def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global val, w, root
        root = tk.Tk()
        top = Toplevel1 (root)
        root.mainloop()
    
w = None
def create_Toplevel1(rt, *args, **kwargs):
        '''Starting point when module is imported by another module.
           Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
        global w, w_win, root
        #rt = root
        root = rt
        w = tk.Toplevel (root)
        top = Toplevel1 (w)
        autosave_support.init(w, top, *args, **kwargs)
        return (w, top)
    
def destroy_Toplevel1():
        global w
        w.destroy()
        w = None
    
class Toplevel1:
       def __init__(self, top=None):
           '''This class configures and populates the toplevel window.
              top is the toplevel containing window.'''
           _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
           _fgcolor = '#000000'  # X11 color: 'black'
           _compcolor = '#d9d9d9' # X11 color: 'gray85'
           _ana1color = '#d9d9d9' # X11 color: 'gray85'
           _ana2color = '#ececec' # Closest X11 color: 'gray92'
   
           top.geometry("1920x1017+97+0")
           top.minsize(120, 1)
           top.maxsize(1920, 1080)
           top.resizable(1,  1)
           top.title("New Toplevel")
           top.configure(background="#d9d9d9")
           top.configure(highlightbackground="#d9d9d9")
           top.configure(highlightcolor="black")
   
           self.Label1 = tk.Label(top)
           self.Label1.place(relx=0.0, rely=0.0, height=60, width=1920)
           self.Label1.configure(activebackground="#f9f9f9")
           self.Label1.configure(activeforeground="black")
           self.Label1.configure(background="#f5ffb3")
           self.Label1.configure(disabledforeground="#a3a3a3")
           self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
           self.Label1.configure(foreground="#ff0000")
           self.Label1.configure(highlightbackground="#d9d9d9")
           self.Label1.configure(highlightcolor="black")
           self.Label1.configure(text='''Hệ thống quản lý sinh viên môn học''')
   
           self.Frame1 = tk.Frame(top)
           self.Frame1.place(relx=0.005, rely=0.079, relheight=0.861
                   , relwidth=0.981)
           self.Frame1.configure(relief='groove')
           self.Frame1.configure(borderwidth="2")
           self.Frame1.configure(relief="groove")
           self.Frame1.configure(background="#F2F2F2")
           self.Frame1.configure(highlightbackground="#d9d9d9")
           self.Frame1.configure(highlightcolor="black")
   
           self.Label2 = tk.Label(self.Frame1)
           self.Label2.place(relx=0.037, rely=0.079, height=668, width=469)
           self.Label2.configure(activebackground="#f9f9f9")
           self.Label2.configure(activeforeground="black")
           self.Label2.configure(background="#d9d9d9")
           self.Label2.configure(disabledforeground="#a3a3a3")
           self.Label2.configure(foreground="#000000")
           self.Label2.configure(highlightbackground="#d9d9d9")
           self.Label2.configure(highlightcolor="black")
   
           self.Label3 = tk.Label(self.Frame1)
           self.Label3.place(relx=0.377, rely=0.079, height=51, width=235)
           self.Label3.configure(activebackground="#f9f9f9")
           self.Label3.configure(activeforeground="black")
           self.Label3.configure(background="#F32463")
           self.Label3.configure(disabledforeground="#a3a3a3")
           self.Label3.configure(font="-family {Segoe UI} -size 24 -weight bold")
           self.Label3.configure(foreground="#ffffff")
           self.Label3.configure(highlightbackground="#d9d9d9")
           self.Label3.configure(highlightcolor="black")
           self.Label3.configure(text='''Nguyễn Văn A''')
   
           self.Label4 = tk.Label(self.Frame1)
           self.Label4.place(relx=0.382, rely=0.194, height=60, width=221)
           self.Label4.configure(activebackground="#f9f9f9")
           self.Label4.configure(activeforeground="black")
           self.Label4.configure(background="#F2F2F2")
           self.Label4.configure(disabledforeground="#a3a3a3")
           self.Label4.configure(font="-family {Segoe UI} -size 22 -weight bold")
           self.Label4.configure(foreground="#000000")
           self.Label4.configure(highlightbackground="#d9d9d9")
           self.Label4.configure(highlightcolor="black")
           self.Label4.configure(text='''Số thứ tự''')
   
           self.Label4_1 = tk.Label(self.Frame1)
           self.Label4_1.place(relx=0.382, rely=0.377, height=60, width=221)
           self.Label4_1.configure(activebackground="#f9f9f9")
           self.Label4_1.configure(activeforeground="black")
           self.Label4_1.configure(background="#F2F2F2")
           self.Label4_1.configure(disabledforeground="#a3a3a3")
           self.Label4_1.configure(font="-family {Segoe UI} -size 22 -weight bold")
           self.Label4_1.configure(foreground="#000000")
           self.Label4_1.configure(highlightbackground="#d9d9d9")
           self.Label4_1.configure(highlightcolor="black")
           self.Label4_1.configure(text='''Date''')
   
           self.Label4_2 = tk.Label(self.Frame1)
           self.Label4_2.place(relx=0.382, rely=0.285, height=58, width=221)
           self.Label4_2.configure(activebackground="#f9f9f9")
           self.Label4_2.configure(activeforeground="black")
           self.Label4_2.configure(background="#F2F2F2")
           self.Label4_2.configure(disabledforeground="#a3a3a3")
           self.Label4_2.configure(font="-family {Segoe UI} -size 22 -weight bold")
           self.Label4_2.configure(foreground="#000000")
           self.Label4_2.configure(highlightbackground="#d9d9d9")
           self.Label4_2.configure(highlightcolor="black")
           self.Label4_2.configure(text='''Mã Sinh Viên''')
   
           self.Label4_1_1 = tk.Label(self.Frame1)
           self.Label4_1_1.place(relx=0.382, rely=0.468, height=57, width=221)
           self.Label4_1_1.configure(activebackground="#f9f9f9")
           self.Label4_1_1.configure(activeforeground="black")
           self.Label4_1_1.configure(background="#F2F2F2")
           self.Label4_1_1.configure(disabledforeground="#a3a3a3")
           self.Label4_1_1.configure(font="-family {Segoe UI} -size 22 -weight bold")
           self.Label4_1_1.configure(foreground="#000000")
           self.Label4_1_1.configure(highlightbackground="#d9d9d9")
           self.Label4_1_1.configure(highlightcolor="black")
           self.Label4_1_1.configure(text='''Số buổi nghỉ''')
   
           self.Label4_3 = tk.Label(self.Frame1)
           self.Label4_3.place(relx=0.558, rely=0.194, height=60, width=220)
           self.Label4_3.configure(activebackground="#f9f9f9")
           self.Label4_3.configure(activeforeground="black")
           self.Label4_3.configure(background="#d9d9d9")
           self.Label4_3.configure(disabledforeground="#a3a3a3")
           self.Label4_3.configure(font="-family {Segoe UI} -size 22")
           self.Label4_3.configure(foreground="#000000")
           self.Label4_3.configure(highlightbackground="#d9d9d9")
           self.Label4_3.configure(highlightcolor="black")
           self.Label4_3.configure(text='''01''')
   
           self.Label4_4 = tk.Label(self.Frame1)
           self.Label4_4.place(relx=0.558, rely=0.285, height=57, width=220)
           self.Label4_4.configure(activebackground="#f9f9f9")
           self.Label4_4.configure(activeforeground="black")
           self.Label4_4.configure(background="#d9d9d9")
           self.Label4_4.configure(disabledforeground="#a3a3a3")
           self.Label4_4.configure(font="-family {Segoe UI} -size 22")
           self.Label4_4.configure(foreground="#000000")
           self.Label4_4.configure(highlightbackground="#d9d9d9")
           self.Label4_4.configure(highlightcolor="black")
           self.Label4_4.configure(text='''19000404''')
   
           self.Label4_5 = tk.Label(self.Frame1)
           self.Label4_5.place(relx=0.558, rely=0.377, height=57, width=220)
           self.Label4_5.configure(activebackground="#f9f9f9")
           self.Label4_5.configure(activeforeground="black")
           self.Label4_5.configure(background="#d9d9d9")
           self.Label4_5.configure(disabledforeground="#a3a3a3")
           self.Label4_5.configure(font="-family {Segoe UI} -size 22")
           self.Label4_5.configure(foreground="#000000")
           self.Label4_5.configure(highlightbackground="#d9d9d9")
           self.Label4_5.configure(highlightcolor="black")
           self.Label4_5.configure(text='''29/08/2022''')
   
           self.Label4_6 = tk.Label(self.Frame1)
           self.Label4_6.place(relx=0.558, rely=0.468, height=60, width=220)
           self.Label4_6.configure(activebackground="#f9f9f9")
           self.Label4_6.configure(activeforeground="black")
           self.Label4_6.configure(background="#d9d9d9")
           self.Label4_6.configure(disabledforeground="#a3a3a3")
           self.Label4_6.configure(font="-family {Segoe UI} -size 22")
           self.Label4_6.configure(foreground="#000000")
           self.Label4_6.configure(highlightbackground="#d9d9d9")
           self.Label4_6.configure(highlightcolor="black")
           self.Label4_6.configure(text='''01''')
   
if __name__ == '__main__':
    vp_start_gui()