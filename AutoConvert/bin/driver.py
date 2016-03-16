# Import Statements
import subprocess as sp
import os

# Declare Global Variables
FFMPEG = "./ffmpeg.exe"
watchPath = "../IN"
destinationPath = "../OUT"
ffmpegReady = 1

# TODO Write Watch Folder Initialization



# TODO Write File Information Retriever
# Directory Lister
fileQueue = []
for files in os.listdir(watchPath):
    fileQueue.append(files)


# FFMPEG Launcher

# FFMPEG Variables
if len(fileQueue) > 0 and ffmpegReady == 1:
    for f in fileQueue:
        (fileName,fileExtension) = os.path.splitext(fileQueue.pop())
        codec = "libx264"
        command = [ FFMPEG, "-i", watchPath + '/' +fileName + fileExtension, "-c:v", codec, destinationPath + '/' + fileName + ".mp4", ]
        sp.run(command)
