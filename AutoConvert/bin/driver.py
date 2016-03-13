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
fileQueue = []
for files in os.listdir('./IN'):
    info = os.stat(files)
    fileQueue.append(info)


# FFMPEG Launcher

# FFMPEG Variables
if fileQueue.amount() > 0 and ffmpegReady == 1:
    fileName, fileExtension = os.path.splitext(fileQueue.pop(0))
    codec = "libx264"
    command = [FFMPEG,
               'ffmpeg',
               '-c:v', codec,
               destinationPath + fileName + ".mp4"]
    pipe = sp.Popen(command)
