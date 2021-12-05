#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of Tkinter Frame
win.geometry("750x250")

#Define a Label widget
Label(win, text= "Select an Option from the List", font=('Aerial', 14, 'bold')).pack(pady=15)

#Create a Combobox with list of items
var= StringVar()
my_combobox= ttk.Combobox(win, textvariable=var, values=["High", "Mid","Low"], state= 'disabled')
my_combobox.pack()

#Create a Button widget
win.mainloop()