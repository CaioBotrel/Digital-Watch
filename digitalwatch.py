from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file('digital-7.ttf')

color1 = "#000000"
color2 = "#FFFAFA"
color3 = "#90EE90"
color4 = "#FF0000"
color5 = "#C0C0C0"
color6 = "#00BFFF"

background = color1
color = color2
time = datetime.now()

window = Tk()
window.title('Digital Watch')
window.geometry('320x180')
window.resizable(width=FALSE, height=FALSE)
window.configure(background=color1)


def clock():
 time = datetime.now()

 hour = time.strftime('%H:%M:%S')
 day_of_the_week = time.strftime('%A')
 day = time.day
 month = time.strftime('%b') # if you use b instead of B, it will show the abreviation of the month
 year = time.strftime('%Y')

 label1.config(text=hour)
 label1.after(100, clock)
 label2.config(text=day_of_the_week + '      ' + str(day)+ '/' + str(month) + '/' + str(year))


label1=Label(window, text='', font=('digital-7 80'), background=background, fg=color)
label1.grid(row=0, column=0, sticky=NW, padx=5)
label2=Label(window, text='', font=('digital-7 20'), background=background, fg=color)
label2.grid(row=1, column=0, sticky=NW, padx=5)


clock()
window.mainloop()