from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p") # setup time directive
    time_label.config(text=time_string)

    date_string = strftime("%a, %B %d,%Y ") # setup date directive
    date_label.config(text=date_string)

    window.after(1000,update) # update the window after 1000ms

# creating the window
window = Tk()
window.title("Digital clock")

time_label = Label(window,font=("Arial",50),fg="red3",bg="snow") # setup time label (font,size,color,background)
time_label.pack()

date_label = Label(window,font=("Arial",20),fg="dark green") # setup date label (font,size,color)
date_label.pack()


update() # recall function
window.mainloop()