import xml.etree.ElementTree as eT
from tkinter import *
import driver
# FFmpeg variables


# TODO User Interface
def user_interface():
    get_past_settings()
    global win
    win = Tk()
    win.geometry("500x350")
    win.title(" CCCP - Auto Codec Converter")
    msg = Label(win, width = 25, text = "Watch folder")
    msg.grid(row=1,column=1,pady=5)
    eqn = Entry(win, width=25)
    eqn.grid(row=2,column=1,pady=5)
    msg = Label(win, width = 25, text = "Destination folder")
    msg.grid(row=3,column=1,pady=5)
    eqn = Entry(win, width=25)
    eqn.grid(row=4,column=1,pady=5)
    bitext = Label(win, width = 25, text = "Bit Rate").grid(row=5,column=1,pady=2)
    bitslide = Scale(win, from_=0, to=5, orient=HORIZONTAL).grid(row=6,column=1,pady=5)
    msg2 = Label(win, width = 25, text = "Choose codec to convert to")
    msg2.grid(row=7,column=1,pady=5)
    vary = StringVar(win)
    vary.set("AVI")
    ops = OptionMenu(win,vary,"GoPro Cineform","AVI","DNxRAW")
    ops.configure(width=25)
    ops.grid(row=8,column=1,pady=5)
    #TODO HIGH QUAL SETTINGS
    active = Button(win,text = "Begin Conversion",command = start_convert)
    active.grid(row=10,column=2,pady=5)
    

    msg3 = Label(win, width = 25, text = "Choose Aspect Ratio")
    msg3.grid(row=1,column=3,pady=5)
    #TODO Fix the Aspect Ratio area
    #opsr = Listbox(win,height = 5)
    #opsr.grid(row=5,column=3,pady=5)
    #opsr.insert(1, "Auto")
    #opsr.insert(2, "4:3")
    #opsr.insert(3, "16:9")
    #opsr.insert(4, "1.3333")
    #opsr.insert(5, "1.7777")
    win.mainloop()

def start_convert():
    #xml_write()
    win.destroy()
    driver.start_up_protocol()
    
# TODO Get Past Settings
def get_past_settings():
    root = eT.parse('user_prefs.xml').getroot()
    # Declare and set User Preferences
    global pastSettings
    pastSettings = {}
    pastSettings["watch_folder"] = root[0][0].text
    pastSettings["destination_folder"] = root[0][1].text
    pastSettings["video_codec"] = root[0][2].text
    pastSettings["video_param"] = root[0][3].text
    #pastSettings["audio_codec"] = root[0][4].text #
    #pastSettings["audio_param"] = root[0][5].text
    pastSettings["force_aspect"] = root[0][6].text
    pastSettings["aspect"] = root[0][7].text


# TODO Validate Settings


# TODO Post Settings

user_interface()
