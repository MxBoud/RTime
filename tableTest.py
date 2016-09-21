from Tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)


import tktable

table = tktable.Table(parent, 
    rows = 5,
    cols = 5
    )
table.pack()

mainloop()