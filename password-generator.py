from tkinter import *
import string
import random
import hashlib



window = Tk()
window.title("App")
top = Frame(window)
top.pack()
bottom = Frame(window)
bottom.pack(side=BOTTOM)

title = Label(top,text="Password Generator")
title.place(x=25,y=25,anchor="center")
title.pack(side="top")


#radio buttons
value = IntVar()
r1 = Radiobutton(top,text="Low",variable=value,value=8)
r1.place(anchor="center")
r1.pack(side="bottom")

r2 = Radiobutton(top,text="Medium",variable=value,value=12)
r2.place(anchor="center")
r2.pack(side="bottom")

r3 = Radiobutton(top,text="Strong",variable=value,value=15)
r3.place(anchor="center")
r3.pack(side="bottom")

#display label
global entry
entry= Entry(bottom)
entry.pack()

#password-generator
def gen_password():
    #global password
    symbols=['~','!','@','#','$','%','^','&','*','(',')','-','=','{','}','<','>','?','/','+']
    letters_digits=string.ascii_letters+string.digits

    #generate random string
    random_string = ''.join(random.choice(letters_digits) for i in range(value.get()))

    #generate random symbols
    random_symbols = ''.join(random.choice(symbols) for i in range(value.get()//3))

    #combine them and shuffle
    random_string_symbols = list(random_string+random_symbols)
    random.shuffle(random_string_symbols)
    shuffle = ''.join(random_string_symbols)

    #generate hash value for the combined string
    hash_value = hashlib.sha256(shuffle.encode())
    random_int = random.randint(0,10)
    #choose random 4 characeters from hash value
    hash_value = hash_value.hexdigest()[random_int:random_int+3]

    #add it to the shuffle string and shuffle
    password = list(shuffle+hash_value)
    random.shuffle(password)
    
    password= "".join(password[:-3])
    entry.delete(0,END)
    entry.insert(0,password)



#reset function
def clear():
    entry.delete(0,END)
    

#enter button
enter = Button(bottom,text="Enter",command=gen_password)
enter.place(anchor="center")
enter.pack(side="left",padx=10)


#reset button
reset = Button(bottom,text="Reset",command=clear)
reset.place(anchor="center")
reset.pack(side="left",padx=10)














window.mainloop()
