import Tkinter as tk
import tktable

root = tk.Tk()
table = tktable.Table(root, rows=10, cols=4)
table.pack(side="top", fill="both", expand=True)
root.mainloop()