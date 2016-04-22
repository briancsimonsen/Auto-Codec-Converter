import xml.etree.ElementTree as eT
from math import ceil
from tkinter import *

import driver


# FFmpeg variables


# TODO User Interface
def user_interface():
    get_past_settings()

    # Creates a dictionary to store the new information using old information
    currSettings = {}
    currSettings["watch_folder"] = pastSettings["watch_folder"]
    currSettings["destination_folder"] = pastSettings["destination_folder"]
    currSettings["video_codec"] = pastSettings["video_codec"]
    currSettings["video_param_mod"] = 1
    currSettings["force_aspect"] = pastSettings["force_aspect"]
    currSettings["aspect"] = pastSettings["aspect"]
    currSettings["hq"] = False

    # establishes TK Window
    global win
    win = Tk()
    win.geometry("475x360")
    win.title(" CCCP - Auto Codec Converter")
    win.resizable(width=FALSE, height=FALSE)

    # input filepath
    msg = Label(win, width=25, text="Watch folder")
    msg.grid(row=1, column=1, pady=5, columnspan=2)
    inP = Entry(win, width=29)
    inP.insert(0, currSettings["watch_folder"])
    inP.grid(row=2, column=1, pady=5, columnspan=2)

    # Button for the input filepath
    def inBrowse():
        currSettings["watch_folder"] = filedialog.askdirectory(initialdir="C:\\")
        inP.delete(0, END)
        inP.insert(0, currSettings["watch_folder"])
        if(inP.get()==""):
            inP.insert(0,pastSettings["watch_folder"])
            currSettings["watch_folder"] = pastSettings["watch_folder"]

    inButton = Button(win, text="Browse", command=inBrowse)
    inButton.grid(row=2, column=3, pady=5)

    # Destination folder
    msg = Label(win, width=25, text="Destination folder")
    msg.grid(row=3, column=1, pady=5, columnspan=2)
    outP = Entry(win, width=29)
    outP.insert(0, currSettings["destination_folder"])
    outP.grid(row=4, column=1, pady=5, columnspan=2)

    # Button for the output filepath
    def outBrowse():
        currSettings["destination_folder"] = filedialog.askdirectory(initialdir="C:\\")
        outP.delete(0, END)
        outP.insert(0, currSettings["destination_folder"])
        if(outP.get()==""):
            outP.insert(0,pastSettings["destination_folder"])
            currSettings["destination_folder"] = pastSettings["destination_folder"]

    outButton = Button(win, text="Browse", command=outBrowse)
    outButton.grid(row=4, column=3, pady=5)

    # Bitrate and Slider
    bitext = Label(win, width=25, text="        Bit Rate")
    bitext.grid(row=5, column=1, pady=2)
    bitvar = DoubleVar()

    def bitrModSet(value):
        currSettings["video_param_mod"] = (1 / 50.0) * bitvar.get()

    bitslide = Scale(win, variable=bitvar, from_=0, to=50, orient=HORIZONTAL, length=175, command=bitrModSet)
    bitslide.set(50)
    bitslide.grid(row=6, column=1, pady=5, columnspan=2)

    # Codec Dropdown
    msg2 = Label(win, width=25, text="Output Codec")
    msg2.grid(row=7, column=1, pady=5, columnspan=2)
    vary = StringVar(win)
    vary.set(currSettings["video_codec"])

    def cSet(x):
        currSettings["video_codec"] = x

    codecz = []
    library = eT.parse('codec_library.xml').getroot()
    for node in library[0].iter('encoder'):
        for codec in node.iter('codec'):
            codecz.append(codec.text)
    list.sort(codecz)
    ops = OptionMenu(win, vary, *codecz, command=cSet)
    ops.configure(width=25)
    ops.grid(row=8, column=1, pady=5, columnspan=2)

    # High Quality Settings
    vary2 = IntVar(win)
    vary2.set(currSettings["hq"])

    def hqSet():
        if (currSettings["hq"]):
            currSettings["video_param_mod"] = (1 / 50.0) * bitvar.get()
            currSettings["hq"] = False
        else:
            currSettings["video_param_mod"] = 1
            currSettings["hq"] = True

    hqs = Checkbutton(win, text="Force High Quality Settings", variable=vary2, onvalue=1, offvalue=0, command=hqSet)
    hqs.grid(row=9, column=1, pady=5, columnspan=2)

    # Aspect Ratio
    msg3 = Label(win, width=25, text="Choose Aspect Ratio")
    msg3.grid(row=1, column=4, pady=5)

    def radSet():
        currSettings["aspect"] = vary3.get()
        if(currSettings["aspect"] != "Auto"):
            currSettings["force_aspect"] = True
        else:
            currSettings["force_aspect"] = False

    vary3 = StringVar()
    vary3.set(currSettings["aspect"])
    opsr1 = Radiobutton(win, variable=vary3, text="Auto", value="Auto", command=radSet)
    opsr1.grid(row=2, column=4, pady=3)
    opsr2 = Radiobutton(win, variable=vary3, text="3:2", value="3:2", command=radSet)
    opsr2.grid(row=3, column=4, pady=3)
    opsr3 = Radiobutton(win, variable=vary3, text="4:3", value="4:3", command=radSet)
    opsr3.grid(row=4, column=4, pady=3)
    opsr4 = Radiobutton(win, variable=vary3, text="11:8", value="11:8", command=radSet)
    opsr4.grid(row=5, column=4, pady=3)
    opsr5 = Radiobutton(win, variable=vary3, text="16:9", value="16:9", command=radSet)
    opsr5.grid(row=6, column=4, pady=3)

    # Activation Button


    def start_convert():
        # if(not(isValid())):
        # print terrible things
        # else:
        postSettings(currSettings)
        win.destroy()
        driver.start_up_protocol()

    active = Button(win, text="Begin Conversion", command=start_convert)
    active.grid(row=10, column=2, pady=5,columnspan=2)

    # Mainloop
    win.mainloop()


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
    pastSettings["force_aspect"] = root[0][6].text
    pastSettings["aspect"] = root[0][7].text


# TODO Validate Settings


# TODO Post Settings
def postSettings(dicto):
    tree = eT.parse('user_prefs.xml')
    root = tree.getroot()
    # Declare and set User Preferences
    # global pastSettings
    # pastSettings = {}
    root[0][0].text = str(dicto["watch_folder"])
    root[0][1].text = str(dicto["destination_folder"])
    root[0][2].text = str(dicto["video_codec"])
    # Write the Codec param using the codec info
    library = eT.parse('codec_library.xml').getroot()
    # iterate through encoders to look for correct codec to get encoder characteristics
    pMin = 0
    pMax = 0
    for node in library.iter('encoder'):
        for codec in node.iter('codec'):
            if codec.text == str(dicto["video_codec"]):
                pMin = int(node[2].text)
                pMax = int(node[3].text)
    pInt = pMax - pMin
    pVal = pInt * float(dicto["video_param_mod"])
    pVal = int(ceil(pVal))
    if (pInt < 0):
        pVal *= -1
        setter = pMin - pVal
    else:
        setter = pMin + pVal
    root[0][3].text = str(setter)
    root[0][6].text = str(dicto["force_aspect"])
    root[0][7].text = str(dicto["aspect"])
    tree.write('user_prefs.xml')  # user_prefs


user_interface()
