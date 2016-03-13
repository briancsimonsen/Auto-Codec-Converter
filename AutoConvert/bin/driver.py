# Import Statements
import subprocess as sp

# Declare Global Variables
FFMPEG = "/bin/ffmpeg.exe"

# TODO Write Watch Folder Initialization



# TODO Write File Information Retriever



# FFMPEG Launcher

# FFMPEG Variables
watchPath = ""
destinationPath = ""
fileName = "example"
fileExtension = "mp4"
codec = "dnxhd"

# Command
command = [ FFMPEG,
            '-i', watchPath + fileName + fileExtension,
            '-c:v', codec,
            destinationPath + fileName + ".mxf"]