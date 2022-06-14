# import tkinter
from tkinter import *

# create a window
root = Tk()

# create a label
hello = Label(root, text='hello')

# display the label in the window
hello.grid(row=0,column=0)

# another one
goodbye = Label(root, text='goodbye')
goodbye.grid(row=1, column=0)

# create a function
def been_clicked():
    print('click')

# create a button and place it on the second row   
btn = Button(root, text='Click me', command=been_clicked)    
btn.grid(row=2, column=0)

# have a box to enter things. user input
ent = Entry(root)
ent.grid(row=3,column=0)

# get the text from the user input
print(ent.get())

# Don't be able to change the size of the box
root.resizable(width=False, height=False)