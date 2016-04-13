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
    #user_interface.user_interface()
    get_settings()
    validate_file_path()
    run()


def get_settings():
    root = eT.parse('user_prefs.xml').getroot()
    global watch_folder
    global destination_folder
    global video_codec
    global video_param
    global audio_codec
    global audio_param
    global force_aspect
    global aspect
    global force_copyright
    global copyright
    watch_folder = root[0][0].text
    destination_folder = root[0][1].text
    video_codec = root[0][2].text
    video_param = root[0][3].text
    audio_codec = root[0][4].text
    audio_param = root[0][5].text
    force_aspect = root[0][6].text
    aspect = root[0][7].text
    force_copyright = root[0][8].text
    copyright = root[0][9].text


# Validate File Path
def validate_file_path():
    if not os.path.exists(watch_folder):
        os.makedirs(watch_folder)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)


def file_add():
    for files in os.listdir(watch_folder):
        if not(files in fileQueue):
            fileQueue.append(files)


# FFMPEG Variables
def run():
    while True:
        file_add()
        if len(fileQueue) > 0 and ffmpegReady == 1:
            for f in fileQueue:
                (file_name, file_extension) = os.path.splitext(fileQueue.pop())
                command = [FFMPEG,
                           "-i", watch_folder + '/' + file_name + file_extension,
                           video_codec, "-crf", video_param,
                           destination_folder + '/' + file_name + ".mp4",
                           ]
                sp.check_output(command)
                os.remove(watch_folder + '/' + file_name + file_extension)
                sleep(5)
