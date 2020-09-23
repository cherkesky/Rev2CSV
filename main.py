from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, colorchooser


root=Tk()
root.winfo_toplevel().title("Rev2CSV")

canvas = Canvas(root, width = 1200, height = 350)      
canvas.pack()    
img = PhotoImage(file="logo.png")   
canvas.create_image(20,20, anchor=NW, image=img)      

answer = simpledialog.askstring("PID", "What is your PID?",parent=root)
print (answer)
root.destroy()

root.mainloop()