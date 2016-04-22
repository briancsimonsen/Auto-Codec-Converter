# Import Statements
import os
import subprocess as sp
import xml.etree.ElementTree as eT
from time import sleep

import user_interface

# Declare Global Variables
FFMPEG = "./ffmpeg.exe"
ffmpegReady = 1
fileQueue = []
global video_extentions


def start_process():
    user_interface.user_interface()


# Start Up Protocol
def start_up_protocol():
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
    force_aspect = bool(root[0][6].text)
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
        (file_name, old_file_extension) = os.path.splitext(files)
        if(old_file_extension in video_extentions):
            amt1 = os.stat(watch_folder + "/" + files).st_size
            sleep(3)
            amt2 = os.stat(watch_folder + "/" + files).st_size
            if (not (files in fileQueue) and amt1 == amt2):
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


video_extentions = ['.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d', '.787', '.89', '.aaf',
                    '.aec', '.aep', '.aepx', '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim',
                    '.aqt', '.arcut', '.arf', '.asf', '.asx', '.avb', '.avc', '.avd', '.avi', '.avp', '.avs', '.avs',
                    '.avv', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik', '.bin', '.bix', '.bmk', '.bnp', '.box',
                    '.bs4', '.bsf', '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine', '.cip',
                    '.clpi', '.cmmp', '.cmmtpl', '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v', '.d3v',
                    '.dat', '.dav', '.dce', '.dck', '.dcr', '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb',
                    '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss', '.dmx', '.dnc', '.dpa', '.dpg', '.dream', '.dsy',
                    '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms', '.dvx', '.dxr', '.dzm', '.dzp', '.dzt',
                    '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz', '.fcp', '.fcproject',
                    '.ffd', '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts', '.gvi',
                    '.gvp', '.h264', '.hdmov', '.hkm', '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf', '.ism',
                    '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs', '.izz', '.izzy', '.jss', '.jts', '.jtv', '.k3g',
                    '.kmv', '.ktn', '.lrec', '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21', '.m21', '.m2a', '.m2p',
                    '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta', '.mgv', '.mj2', '.mjp',
                    '.mjpg', '.mk3d', '.mkv', '.mmv', '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov',
                    '.movie', '.mp21', '.mp21', '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4', '.mpf',
                    '.mpg', '.mpg2', '.mpgindex', '.mpl', '.mpl', '.mpls', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd',
                    '.mse', '.msh', '.mswmm', '.mts', '.mtv', '.mvb', '.mvc', '.mvd', '.mve', '.mvex', '.mvp', '.mvp',
                    '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv', '.nvc', '.ogm', '.ogv', '.ogx',
                    '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist',
                    '.plproj', '.pmf', '.pmv', '.pns', '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh',
                    '.pssd', '.pva', '.pvr', '.pxv', '.qt', '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz', '.r3d', '.rcd',
                    '.rcproject', '.rdb', '.rec', '.rm', '.rmd', '.rmd', '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp',
                    '.rsx', '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt', '.scc', '.scm', '.scm',
                    '.scn', '.screenflow', '.sec', '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv', '.smi', '.smi',
                    '.smil', '.smk', '.sml', '.smv', '.spl', '.sqz', '.srt', '.ssf', '.ssm', '.stl', '.str', '.stx',
                    '.svi', '.swf', '.swi', '.swt', '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod', '.tp', '.tp0',
                    '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt', '.tvs', '.usf', '.usm', '.vc1', '.vcpf', '.vcr',
                    '.vcv', '.vdo', '.vdr', '.vdx', '.veg', '.vem', '.vep', '.vf', '.vft', '.vfw', '.vfz', '.vgz',
                    '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3', '.vp6', '.vp7', '.vpj',
                    '.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv',
                    '.wmx', '.wot', '.wp3', '.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv',
                    '.xmv', '.xvid', '.y4m', '.yog', '.yuv', '.zeg', '.zm1', '.zm2', '.zm3', '.zmv']
