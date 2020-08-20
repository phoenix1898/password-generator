from tkinter import *

def focusText(event):
   w.config(state='normal')
   w.focus()
   w.config(state='disabled')

master = Tk()

w = Text(master, height=1, borderwidth=0)
w.insert(5.0, "Hello, world!")
w.pack()

w.configure(state="disabled")

w.bind('hello', focusText) 

mainloop()
