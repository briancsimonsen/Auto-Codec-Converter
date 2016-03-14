# Import Statements
import subprocess as sp
import os

# Declare Global Variables
FFMPEG = "/bin/ffmpeg.exe"
watchPath = "./IN"
destinationPath = "./OUT"
ffmpegReady = 1

# TODO Write Watch Folder Initialization



# TODO Write File Information Retriever
# Directory Lister
def ffLaunch():
    fileQueue = []
    for files in os.listdir(watchPath):
        info = os.stat(files)
        fileQueue.append(info)


# FFMPEG Launcher
	
# FFMPEG Variables
    if fileQueue.length() > 0 and ffmpegReady == 1:
        fs = fileQueue[0].split(".")
        fileName = fs[0]
        fileExtension = fs[1]
        codec = "libx264"
        command = [FFMPEG,'-i',
                   watchPath + fileName + fileExtension,
                   '-c:v',
                   codec,destinationPath + fileName + ".mp4"]
        pipe = sp.Popen(command)
