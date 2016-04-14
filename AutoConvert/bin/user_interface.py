import xml.etree.ElementTree as et
from tkinter import *
import driver
# FFmpeg variables



# TODO User Interface
def user_interface():
    get_past_settings()
    win = Tk()
    win.geometry("450x300")
    win.title(" CCCP - Auto Codec Converter")
    msg = Label(win, width = 25, text = "Enter watch folder path here")
    msg.place(x=50,y=25)
    eqn = Entry(win, width=25)
    eqn.place(x=65,y=50)
    msg = Label(win, width = 25, text = "Enter destination folder path here")
    msg.place(x=50,y=75)
    eqn = Entry(win, width=25)
    eqn.place(x=65,y=100)
    msg2 = Label(win, width = 25, text = "Choose codec to convert to")
    msg2.place(x=55,y=125)
    ops = Listbox(win,height = 3)
    ops.place(x=80,y=150)
    ops.insert(1, "GoPro Cineform")
    ops.insert(2, "AVI")
    ops.insert(3, "DNxRAW")
    active = Button(win,text = "Create")
    active.place(x=210,y=230)
    bitext = Label(win, width = 25, text = "Enter Bitrate Here").place(x=240,y=25)

    bit = Entry(win,width = 25)
    bit.insert(0,"30")
    bit.place(x = 255, y=50)

    msg3 = Label(win, width = 25, text = "Choose Aspect Ratio")
    msg3.place(x=235,y=125)
    opsr = Listbox(win,height = 3)
    opsr.place(x=270,y=150)
    opsr.insert(1, "Auto")
    opsr.insert(2, "4:3")
    opsr.insert(3, "16:9")


# TODO Get Past Settings
def get_past_settings():
    driver.get_settings()


# TODO Validate Settings


# TODO Post Settings

