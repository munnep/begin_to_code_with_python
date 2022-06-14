# drawing application
from tkinter import *
root = Tk()

# create the drawing field
c = Canvas(root, width=500, height=500)

# display it
c.grid(row=0, column=0)

# function for the mouse
def mouse_move(event):
    print(event.x,event.y)

# mouse movement    
c.bind('<B1-Motion>', mouse_move)

# create a blue line
c.create_rectangle(100,100,300,200,outline='blue',fill='blue')

# remove the blue line
c.delete(1)

# store the mouse butten you draw
def mouse_move_draw(event):
    c.create_rectangle(event.x-5,event.y-5,event.x+5,event.y+5,fill='red', outline='red')
    
# execute it
c.bind('<B1-Motion>', mouse_move_draw)

    