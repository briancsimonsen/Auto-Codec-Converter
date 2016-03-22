import xml.etree.ElementTree as et

# FFmpeg variables
destination_folder = ""
video_codec = ""
video_param = ""
audio_codec = ""
audio_param = ""
force_aspect = False
aspect = ""
force_copyright = False
copyright = ""


# TODO User Interface
def user_interface():
    get_past_settings()


# TODO Get Past Settings
def get_past_settings():
    root = et.parse('user_prefs.xml').getroot()
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


# TODO Validate Settings


# TODO Post Settings

