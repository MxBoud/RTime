from  tableList import *
from Tkinter import *

root = Tk()
root.title("Temps de reaction")
root.grid()

tl = TableList(root, 
    background = "white",
    columns = (0, "Essai", 0, "Temps de reaction (s)"),
    stretch = "all",
    width = 50,
    setfocus = 1, ###this lets you use keyboard navigation
    activestyle = "none",
    takefocus = 0
    )
tl.grid(column=3,row=2)
tl.pack()
   
def sortbycolumn(table, col):
    """alternate increasing and decreasing order sorts
    """
    order = "-increasing"
    if tl.sortcolumn() == int(col) and tl.sortorder() == "increasing":
        order = "-decreasing"
    tl.sortbycolumn(col, order)
        
#tl.configure(labelcommand = sortbycolumn)
 

def show():
    print tl.getcurselection()
    
b = Button(root, text="Show Selected")
b.grid(column=4,row=2)
b.pack()

l = Label(root, text="Click the column labels to sort")
l.grid(column=0,row=0)
l.pack()


for a in range(10):
    #tl.insert("end", ("Hello " + str((a + 5) % 10), "World " + str(9 - a), str(a)))
    tl.insert("end", (str(a),str(1.33)))

#tl.bind('<<TablelistSelect>>', (lambda event: show()))
root.mainloop()
