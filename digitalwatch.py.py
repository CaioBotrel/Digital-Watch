import os
from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file('digital-7.ttf')

text_color1 = "#000000"
text_color2 = "#FFFAFA"
text_color3 = "#90EE90"
text_color4 = "#FF0000"
text_color5 = "#C0C0C0"
text_color6 = "#00BFFF"

background = text_color1
color = text_color2
time = datetime.now()

window = Tk()
window.title('Digital Watch')
window.geometry('320x180')
window.resizable(width=FALSE, height=FALSE)
window.configure(background=text_color1)

# Initialize variables
alarm_player = None
alarm_id = None

def clock():
    time = datetime.now()

    hour = time.strftime('%H:%M:%S')
    day_of_the_week = time.strftime('%A')
    day = time.day
    month = time.strftime('%b')
    year = time.strftime('%Y')

    label1.config(text=hour)
    label1.after(100, clock)
    label2.config(text=day_of_the_week + '      ' + str(day)+ '/' + str(month) + '/' + str(year))


label1=Label(window, text='', font=("digital-7", 80), background=background, fg=color)
label1.grid(row=0, column=0, sticky=NW, padx=5)
label2=Label(window, text='', font=("digital-7", 20), background=background, fg=color)
label2.grid(row=1, column=0, sticky=NW, padx=5)


clock()

def set_alarm():
    global alarm_id
    now = datetime.now()
    alarm_time = input("Enter the alarm time in the format     00:50:00: ")
    alarm_time = datetime.strptime(alarm_time, "%H:%M:%S")
    time_until_alarm = (alarm_time - now).total_seconds()
    if time_until_alarm < 0:
        print("Invalid alarm time, alarm time should be in the future")
        return
    alarm_id = window.after(int(time_until_alarm * 1000), alarm)

def alarm():
    global alarm_player
    alarm_player = pyglet.media.Player()
    alarm_path = os.path.join(os.path.dirname(__file__), 'alarm.mp3')
    alarm_sound = pyglet.media.load(alarm_path, streaming=False)
    alarm_player.queue(alarm_sound)
    alarm_player.play()
    alarm_player.loop = True

set_alarm_button = tkinter.Button(window, text="Set Alarm", command=set_alarm)
set_alarm_button.grid(row=2, column=0, sticky=NW, padx=5)

def stop_alarm():
    global alarm_player
    global alarm_id
if alarm_player is not None:
   alarm_player.pause()
if alarm_id is not None:
   window.after_cancel(alarm_id)
   alarm_player = None
   window.quit()

stop_alarm_button = tkinter.Button(window, text="Stop Alarm", command=stop_alarm)
stop_alarm_button.grid(row=3, column=0, sticky=NW, padx=5)

window.resizable(width=True, height=True)

window.mainloop()
