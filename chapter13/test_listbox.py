# drawing application
from tkinter import *
root = Tk()

# create a listbox object
lb = Listbox(root)
lb.grid(row=0, column=0)

# insert the first list
lb.insert(0, 'hello')

# list some extra items
lb.insert(1,'goodbye')
lb.insert(0,'top line')
lb.insert(END, 'bottom line')


# 
def on_select(event):
    lb = event.widget
    index = int(lb.currentselection()[0])
    print(lb.get(index))
    
lb.bind('<<ListboxSelect>>', on_select)   