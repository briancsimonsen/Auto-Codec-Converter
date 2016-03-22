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
    user_interface.user_interface()
    get_settings()
    validate_file_path()
    run()


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
                           "-c:v", video_codec,
                           destination_folder + '/' + file_name + ".mp4",
                           ]
                sp.check_output(command)
                os.remove(watch_folder + '/' + file_name + file_extension)
                sleep(5)
run()


def get_settings():
    validate_file_path()
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
    watch_folder = root[0][1]
    destination_folder = root[0][2]
    video_codec = root[0][3]
    video_param = root[0][4]
    audio_codec = root[0][5]
    audio_param = root[0][6]
    force_aspect = root[0][7]
    aspect = root[0][8]
    force_copyright = root[0][9]
    copyright = root[0][10]
