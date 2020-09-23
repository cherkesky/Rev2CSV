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

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (name.get(), pid.get()))
    get_pid('main', name.get())


master = tk.Tk()
tk.Label(master, text="Business Name").grid(row=0)
tk.Label(master, text="Place ID (PID)").grid(row=1)

name = tk.Entry(master)
pid = tk.Entry(master)

name.grid(row=0, column=1)
pid.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
master.mainloop()


# root.mainloop()