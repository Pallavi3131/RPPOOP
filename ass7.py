import tkinter as tk
root= tk.Tk()

label = tk.Label(root,bg="pink",text = "Pallavi Gaikwad",width=60, height= 10)

label1 = tk.Label(root,bg="purple",text = "142103005",width = 60, height =10)
label.pack(padx = 12 , pady = 5 )
label1.pack(pady = 5)

root.mainloop()