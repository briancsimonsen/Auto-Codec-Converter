# Import Statements
import user_interface
import subprocess as sp
import os
import xml.etree.ElementTree as eT
from time import sleep


# Declare Global Variables
FFMPEG = "./ffmpeg.exe"
ffmpegReady = 1
fileQueue = []


# Start Up Protocol
def start_up_protocol():
    # user_interface.user_interface()
    get_settings()
    validate_file_path()
    run()


# Get settings from user_prefs.xml and needed reference data in codec_library.xml
def get_settings():
    # Attach user_prefs.xml
    root = eT.parse('user_prefs.xml').getroot()
    # Declare and set User Preferences
    global watch_folder
    global destination_folder
    global video_codec
    global video_param
    global audio_codec
    global audio_param
    global force_aspect
    global aspect
    global v_codec_param
    global new_file_extension
    watch_folder = root[0][0].text
    destination_folder = root[0][1].text
    video_codec = root[0][2].text
    video_param = root[0][3].text
    audio_codec = root[0][4].text
    audio_param = root[0][5].text
    force_aspect = root[0][6].text
    aspect = root[0][7].text
    # Attach codec_library.xml
    library = eT.parse('codec_library.xml').getroot()
    # iterate through encoders to look for correct codec to get encoder characteristics
    for node in library.iter('encoder'):
        for codec in node.iter('codec'):
            if codec.text == video_codec:
                encoder = node
                break
    v_codec_param = encoder[1].text
    new_file_extension = encoder[6].text


# Validate File Path
def validate_file_path():
    if not os.path.exists(watch_folder):
        os.makedirs(watch_folder)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)


# Add Files to File Queue
def file_add():
    for files in os.listdir(watch_folder):
        amt1 = os.stat(watch_folder+"/"+files).st_size
        sleep(3)
        amt2 = os.stat(watch_folder+"/"+files).st_size 
        if (not(files in fileQueue) and amt1==amt2):
            fileQueue.append(files)


# FFMPEG Variables
def run():
    while True:
        file_add()
        if len(fileQueue) > 0 and ffmpegReady == 1:
            for f in fileQueue:
                (file_name, old_file_extension) = os.path.splitext(fileQueue.pop())
                command = [FFMPEG,
                           " -i ", "\"" + watch_folder + '/' + file_name + old_file_extension + "\"", ' ',
                           v_codec_param, ' ', video_param, ' ', 
                           "\"" + destination_folder + '/' + file_name + new_file_extension + "\""
                           ]
                commandString = ""
                if force_aspect == True:
                    command.append(" -aspect ")
                    command.append(aspect)
                for j in command:
                    commandString += j
                sp.check_output(commandString)
                os.remove(watch_folder + '/' + file_name + old_file_extension)
                sleep(5)
