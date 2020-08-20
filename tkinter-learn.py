from tkinter import *

window = Tk()

#label and textbox
user = Label(window,text ="User Name")
pas = Label(window,text = "Paasword")

enter1 = Entry(window)
enter2 = Entry(window)

user.grid(row=0)
pas.grid(row=3)
enter1.grid(row = 0,column = 3)
enter2.grid(row=3,column = 3)


#checkbox
checkbox = Checkbutton(window,text = "Keep me logged in")
checkbox.grid(row = 5)

#On click event
def printname():
    print("Prakash")

def print_name(event):
    print("Prakash")

#using command to call function    
button1 = Button(window,text = "Click", command=printname)
button1.grid(row = 7)

#using bind to call function
button2 = Button(window,text = "Click2")
button2.grid(row=7,column = 3)
button2.bind("<Button-1>",print_name)





window.mainloop()
