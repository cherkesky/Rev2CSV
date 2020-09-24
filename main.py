# from tkinter import *
# from tkinter import ttk
# from tkinter import simpledialog, colorchooser
# from math import *


# root=Tk()
# root.winfo_toplevel().title("Rev2CSV")

# canvas = Canvas(root, width = 600, height = 175)      
# canvas.pack()    
# img = PhotoImage(file="logo.png")   
# canvas.create_image(20,20, anchor=NW, image=img)      

# answer = simpledialog.askstring("PID", "What is your PID?",parent=root)
# print (answer)
# root.destroy()


import tkinter as tk
from get_pid import get_pid

def run_get_pid():
    pid.configure(state='normal')
    resolved_pid = get_pid('main', name.get())
    pid.insert('end', str(resolved_pid))

root = tk.Tk()
root.winfo_toplevel().title("GetPID")
tk.Label(root, text="Enter Business Name").grid(row=0)
tk.Label(root, text="Place ID (PID) Result:").grid(row=1)

name = tk.Entry(root, width=25)
pid = tk.Entry(root, width=25)
pid.configure(state='disabled')


name.grid(row=0, column=1)
pid.grid(row=1, column=1)

tk.Button(root, 
          text='Search', command=run_get_pid).grid(row=3, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(root, 
          text='Quit', 
          command=root.quit).grid(row=3, 
                                    column=3, 
                                    sticky=tk.W, 
                                    pady=4)

root.mainloop()


