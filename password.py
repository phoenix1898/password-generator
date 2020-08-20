from tkinter import *
import tkinter as tk
import string
import random
import hashlib




def gen_password():
    global password
    symbols=['~','!','@','#','$','%','^','&','*','(',')','-','=','{','}','<','>','?','/','+']
    letters_digits=string.ascii_letters+string.digits

    #generate random string
    random_string = ''.join(random.choice(letters_digits) for i in range(var.get()))

    #generate random symbols
    random_symbols = ''.join(random.choice(symbols) for i in range(var.get()//3))

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
    
    #display the password in selectable text label
    
    



