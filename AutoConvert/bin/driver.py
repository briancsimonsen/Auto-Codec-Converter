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
for files in os.listdir(watchPath):
    info = os.stat(files)
    fileQueue.append(info)


# FFMPEG Launcher

# FFMPEG Variables
if fileQueue.amount() > 0 and ffmpegReady == 1:
    fileName, fileExtension = os.path.splitext(info)
    codec = "libx264"
    command = [FFMPEG,
               '-i', watchPath + fileName + fileExtension,
               '-c:v', codec,
               destinationPath + fileName + ".mp4"]
    pipe = sp.Popen(command)
