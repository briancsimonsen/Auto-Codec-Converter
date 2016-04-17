import xml.etree.ElementTree as eT
from tkinter import *
import driver
import os
# FFmpeg variables


# TODO User Interface
def user_interface():
    get_past_settings()
    #Creates a dictionary to store the new information. using od information
    currSettings = {}
    currSettings["watch_folder"] = pastSettings["watch_folder"]
    currSettings["destination_folder"] = pastSettings["destination_folder"]
    currSettings["video_codec"] = pastSettings["video_codec"]
    currSettings["video_param"] = pastSettings["video_param"]
    currSettings["force_aspect"] = pastSettings["force_aspect"]
    currSettings["aspect"] = pastSettings["aspect"]
    #establishes TK Window
    global win
    win = Tk()
    win.geometry("500x350")
    win.title(" CCCP - Auto Codec Converter")
    #input filepath
    msg = Label(win, width = 25, text = "Watch folder")
    msg.grid(row=1,column=1,pady=5)
    inP = Entry(win, width=25)
    inP.insert(0,currSettings["watch_folder"])
    inP.grid(row=2,column=1,pady=5)
    #Button for the input filepath
    def inBrowse():
        currSettings["watch_folder"] = filedialog.askdirectory()
        inP.delete(0,END)
        inP.insert(0,currSettings["watch_folder"])
    inButton = Button(win,text="Browse",command = inBrowse)
    inButton.grid(row=2,column=2,pady=5)
    #Destination folder
    msg = Label(win, width = 25, text = "Destination folder")
    msg.grid(row=3,column=1,pady=5)
    outP = Entry(win, width=25)
    outP.insert(0,currSettings["destination_folder"])
    outP.grid(row=4,column=1,pady=5)
    #Button for the output filepath
    def outBrowse():
        currSettings["destination_folder"] = filedialog.askdirectory()
        outP.delete(0,END)
        outP.insert(0,currSettings["destination_folder"])
    outButton = Button(win,text="Browse",command = outBrowse)
    outButton.grid(row=4,column=2,pady=5)
    #Bitrate and Slider    
    bitext = Label(win, width = 25, text = "Bit Rate").grid(row=5,column=1,pady=2)
    bitslide = Scale(win, from_=0, to=5, orient=HORIZONTAL).grid(row=6,column=1,pady=5)
    #Codec Dropdown
    msg2 = Label(win, width = 25, text = "Output Codec")
    msg2.grid(row=7,column=1,pady=5)
    vary = StringVar(win)
    vary.set(currSettings["video_codec"])
    
    ops = OptionMenu(win,vary,"GoPro Cineform","AVI","DNxRAW","MPEG-4")
    ops.configure(width=20)
    ops.grid(row=8,column=1,pady=5)
    #TODO HIGH QUAL SETTINGS
    #Activation Button
    active = Button(win,text = "Begin Conversion",command = start_convert)
    active.grid(row=10,column=2,pady=5)
    
    #Aspect Ratio
    msg3 = Label(win, width = 25, text = "Choose Aspect Ratio")
    msg3.grid(row=1,column=3,pady=5)
    opsr = Listbox(win,height = 5)
    opsr.grid(row=2,column=3,pady=5,rowspan=4)
    opsr.insert(1, "Auto")
    opsr.insert(2, "4:3")
    opsr.insert(3, "16:9")
    opsr.insert(4, "1.3333")
    opsr.insert(5, "1.7777")
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
