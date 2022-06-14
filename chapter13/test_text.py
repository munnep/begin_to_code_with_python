# drawing application
from tkinter import *
root = Tk()

# create a text object
t = Text(width=80, height=10)

# generate it
t.grid(row=0, column=0)

# read all the text from the window back
t.get('1.0',END)

# just read the second line
t.get('2.0', '3.0')

# to clear all the text in the box
t.delete('1.0', END)

# insert text in the box
t.insert('1.0', 'New line 1\nNew line 2')