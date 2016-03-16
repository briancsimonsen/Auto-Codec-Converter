# Import Statements
import subprocess as sp
import os
from time import sleep

# Declare Global Variables
FFMPEG = "./ffmpeg.exe"
watchPath = "../IN"
destinationPath = "../OUT"
ffmpegReady = 1
fileQueue = []

def fileAdd():
    for files in os.listdir(watchPath):
        if(not(files in fileQueue)):
            fileQueue.append(files)

# FFMPEG Variables
def run():
    while True:
        fileAdd()
        if len(fileQueue) > 0 and ffmpegReady == 1:
            for f in fileQueue:
                (fileName,fileExtension) = os.path.splitext(fileQueue.pop())
                codec = "libx264"
                command = [ FFMPEG, "-i", watchPath + '/' +fileName + fileExtension, "-c:v", codec, destinationPath + '/' + fileName + ".mp4", ]
                sp.check_output(command)
                os.remove(watchPath + '/' + fileName + fileExtension)
                sleep(5)
run()
