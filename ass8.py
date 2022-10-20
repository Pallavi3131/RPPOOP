from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

root = Tk()
root.title('Assignment no: 8 142103005')

menubar = Menu(root)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)


edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)


help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

def get_input(label=None):
   label.config(text=""+text.get(1.0, "end-1c"))

# Add a text widget
text=Text(root, width=80, height=15)
text.insert(END, "")
text.pack()

#button
b=ttk.Button(root, text="Print", command=get_input)
b.pack()

label=Label(root, text="", font=('Calibre 15'))
label.pack()

root.config(menu = menubar)
mainloop()